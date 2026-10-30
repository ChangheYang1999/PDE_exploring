# Writes data/N4427_extract.json, the fields of c1-n4's N4-427/N4-428 (prefix 47) and prefix 63 records that
# check_N4427.py (R1-054, REVIEWS_v54) uses. A full copy of the four files (about 1.1 MB) would not fit the 20 MB
# artifact limit. Exact strings shorter than 400 characters are copied verbatim; longer exact strings (about 2600
# characters each) are stored as their sha256, which check_N4427.py compares with the sha256 of its own recomputed
# value written as str(Fraction). Mode endpoints: q_lower_exact verbatim and q_upper_exact - q_lower_exact (same
# denominator, short numerator). Only reads R6/c1-n4; writes only data/N4427_extract.json.
# Usage: python3 -B checks/make_N4427_extract.py (from artifacts).
import hashlib, json, os, sys
from fractions import Fraction as Fr

sys.set_int_max_str_digits(0)
N4R = 'RUN_ROOT/numerics_audit_N4/research'
SRC = {'tail_v04': 'candidate016_angular_tail_bound/verification/result_v04.json',
       'tail_v05': 'candidate016_angular_tail_bound/verification/result_v05.json',
       'multi_v02': 'candidate016_multimode_complete_bounds/verification/result_v02.json',
       'multi_v03': 'candidate016_multimode_complete_bounds/verification/result_v03.json'}
HERE = os.path.dirname(os.path.abspath(__file__))
sha = lambda b: hashlib.sha256(b).hexdigest()
out = {'sources': {}, 'records': {}}
raw = {}
for k, p in SRC.items():
    b = open(os.path.join(N4R, p), 'rb').read()
    raw[k] = json.loads(b)
    out['sources'][k] = {'path': 'research/' + p, 'sha256': sha(b)}
N18 = json.load(open(os.path.join(HERE, 'data', 'N4418_result_v01.json')))


def exact_field(d, key, v):
    Fr(v)
    assert str(Fr(v)) == v, ('not in lowest terms', key)
    if len(v) < 400:
        d[key] = v
    else:
        d[key + '_sha256'] = sha(v.encode())


for k, r in raw.items():
    d = {}
    for key, v in r.items():
        if key in ('inputs', 'checks', 'modes', 'selected_modes', 'Q_prefix_ball', 'S_prefix_ball', 'display_bounds_exact'):
            continue
        if isinstance(v, str) and key.endswith('_exact'):
            exact_field(d, key, v)
        else:
            d[key] = v
    d['checks_all_true'] = all(v is True for v in r['checks'].values())
    d['checks_len'] = len(r['checks'])
    d['inputs'] = {p: h for p, h in r['inputs'].items()
                   if 'candidate016_angular_tail_bound/verification/result_' in p
                   or 'comparison_G0_rF_G1_P2' in p or 'negative_norm_forcing_assembly/verification/result.json' in p
                   or 'candidate016_mode_hardy/verification/mode_' in p}
    if 'display_bounds_exact' in r:
        d['display_bounds_exact'] = r['display_bounds_exact']
    if 'selected_modes' in r:
        if r['selected_modes'] == N18['selected_modes']:
            d['selected_modes_equal_N4418'] = True
        else:
            d['selected_modes'] = r['selected_modes']
    if 'modes' in r:
        d['mode_records'] = [[int(m['n']), m['record'], m['sha256'], m['group_count'], m['accuracy_bits'],
                              m['replay_contains_source_final'], m['source_final_contains_replay']] for m in r['modes']]
    out['records'][k] = d
m4, m5 = raw['tail_v04']['modes'], raw['tail_v05']['modes']
assert [(a['q_lower_exact'], a['q_upper_exact'], a['sha256']) for a in m4] == \
       [(a['q_lower_exact'], a['q_upper_exact'], a['sha256']) for a in m5[:len(m4)]]
out['records']['tail_v04']['modes_equal_first_of_tail_v05'] = len(m4)
q = []
for m in m5:
    lo, hi = Fr(m['q_lower_exact']), Fr(m['q_upper_exact'])
    assert str(lo) == m['q_lower_exact'] and str(hi) == m['q_upper_exact']
    q.append([int(m['n']), m['q_lower_exact'], str(hi - lo)])
out['q_modes_tail_v05'] = q
p = os.path.join(HERE, 'data', 'N4427_extract.json')
s = json.dumps(out, indent=1, sort_keys=True) + '\n'
open(p, 'w').write(s)
print('wrote', p, len(s), 'bytes, sha256', sha(s.encode()))
for k, v in out['sources'].items():
    print(k, v['path'], v['sha256'])
