"""Fixtures for farfield860 v3 (exact rational engine): the verifier's eight topic 39/43 cases (c4-ver scripts/check_exact_tail_sectors.py) and the lead's 09:16Z requirements.
Pure Python (no guard needed). Usage: test_farfield860_v3.py <out.json>"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, sys, time, math
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import farfield860 as FF
import hashlib as _hl
OUT = Path(sys.argv[1]); res = {'version': FF.VERSION, 'source': FF.__file__, 'source_sha256': _hl.sha256(open(FF.__file__, 'rb').read()).hexdigest(), 'script_sha256': _hl.sha256(open(__file__, 'rb').read()).hexdigest(), 'cases': {}}   # E10
def record(name, ok, **info): res['cases'][name] = {'passed': bool(ok), **info}; print(name, 'PASS' if ok else 'FAIL', json.dumps(info, default=str)[:260], flush=True)
seed = json.loads(Path(((_artifact_root + "/outputs") + '/campaign860/seed/seed_860.json')).read_text())
cases = {}
for name, cl in [('zero', 1.8), ('radial', 1.8), ('rounded_moment', 1.8), ('tiny_F0', 1.8), ('ratio_overflow', 1.8), ('seed_stored_decimals', seed['cl']), ('collision_c2', 2.), ('collision_c3', 3.)]:
    a = [Decimal(0)]*860
    if name == 'seed_stored_decimals': a = list(map(Decimal, seed['a_canonical_decimal50']))
    elif name == 'rounded_moment': a[0], a[1], a[2] = Decimal(1), Decimal.from_float(2.**-200), Decimal(-1)
    elif name in ('tiny_F0', 'ratio_overflow'):
        a[0] = Decimal.from_float(1e-100)
        if name == 'ratio_overflow': a[FF.index(1, 0, 0)] = Decimal(1)
    elif name != 'zero': a[0] = Decimal(1)
    if name.startswith('collision_'):
        for j in range(4):
            for m in range(4): a[FF.index(j, m, m)] = Decimal((j+1)*(m+2))/Decimal(8)
    t0 = time.perf_counter(); rep = FF.analyze(a, cl); sec = time.perf_counter()-t0
    try: json.dumps(rep, allow_nan=False); strict_ok = True
    except ValueError as e: strict_ok = False
    cases[name] = rep; lead = rep['actual_leading_density_power']
    print(name, 'seconds %.2f' % sec, 'determined', lead['determined'], 'exp', lead['exponent_exact'], 'growth', lead['growth'], 'E1', rep['E']['1']['L2'], 'I3', rep['E']['3']['scale_invariant_ratio_I_N'], rep['E']['3']['I_N_null_reason'], 'poisson', rep['poisson_sector_identity_exact'], 'strict_json', strict_ok, flush=True)
    res['cases'][name+'_strict_json'] = {'passed': strict_ok}
    res['cases'][name+'_poisson_identity_exact'] = {'passed': rep['poisson_sector_identity_exact'], 'failures': rep['poisson_identity_failures']}
L18 = '900719925474099/8106479329266893'
record('zero_undetermined', cases['zero']['actual_leading_density_power']['determined'] is False and cases['zero']['original_density_residual_grows'] is None and cases['zero']['actual_leading_density_power']['growth'] is None)
for n in ('radial', 'rounded_moment', 'tiny_F0', 'ratio_overflow'):
    L = cases[n]['actual_leading_density_power']; record(n+'_determined_grows', L['determined'] is True and L['exponent_exact'] == L18 and L['growth'] == 'grows' and cases[n]['original_density_residual_grows'] is True, exponent=L['exponent_exact'])
record('rounded_moment_exact_q0_moment', cases['rounded_moment']['tail_moments_C_mjq']['0,0,0'] == str(Decimal(1)/Decimal(2**200)) or Fraction(Decimal(cases['rounded_moment']['tail_moments_C_mjq']['0,0,0'])) != 0, moment=cases['rounded_moment']['tail_moments_C_mjq']['0,0,0'][:40])
E3 = cases['ratio_overflow']['E']['3']; record('ratio_overflow_I3_null_with_reason', E3['scale_invariant_ratio_I_N'] is None and E3['I_N_null_reason'] is not None and 'overflow' in E3['I_N_null_reason'], reason=E3['I_N_null_reason'], decimal=E3['I_N_decimal'])
S = cases['seed_stored_decimals']; LS = S['actual_leading_density_power']; norms = [S['E'][k]['L2'] for k in ('1', '2', '3')]; ref = [0.4403534214951261, 6.363132453703604, 31.72147169432992]
record('seed_exponent_and_norms', LS['determined'] is True and LS['exponent_exact'] == '860221935092683/8146977319648309' and all(abs(n-r)/r <= 1e-12 for n, r in zip(norms, ref)) and LS['growth'] == 'grows' and S['original_density_residual_grows'] is True, exponent=LS['exponent_exact'], norms=norms, leading_norm=LS['coefficient_L2'])
record('seed_E00_structural_zero', [s for s in S['sectors'] if (s['h'], s['q']) == (0, 0)][0]['classification'] == 'structural_zero')
C2 = cases['collision_c2']['actual_leading_density_power']; C3 = cases['collision_c3']['actual_leading_density_power']
record('collision_c2', C2['determined'] is True and C2['exponent_exact'] == '0/1' and C2['growth'] == 'bounded_nondecaying' and len(cases['collision_c2']['exact_exponent_collisions']) > 0, exponent=C2['exponent_exact'], collisions=len(cases['collision_c2']['exact_exponent_collisions']))
record('collision_c3', C3['determined'] is True and C3['exponent_exact'] == '-1/3' and C3['growth'] == 'decays' and len(cases['collision_c3']['exact_exponent_collisions']) > 0, exponent=C3['exponent_exact'], collisions=len(cases['collision_c3']['exact_exponent_collisions']))
res['passed'] = all(c['passed'] for c in res['cases'].values()); OUT.write_text(json.dumps(res, indent=1, default=str)+'\n'); print('ALL PASSED' if res['passed'] else 'SOME FAILED')
