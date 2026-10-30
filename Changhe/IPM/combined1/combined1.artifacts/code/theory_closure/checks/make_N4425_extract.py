#!/usr/bin/env python3
# Writes checks/data/N4425_extract.json (or the path given as argv[1]): fields copied verbatim from c1-n4's
# research/candidate017_dual_residual_replay/verification/result.json, mode_001.json and mode_003.json (N4-425),
# which are read only. Used by check_N4425.py (review R1-053, Part D).
import json, hashlib, os, sys
V = 'RUN_ROOT/numerics_audit_N4/research/candidate017_dual_residual_replay/verification/'
dest = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data',
                                                           'N4425_extract.json')


def sh(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


R = json.load(open(V + 'result.json'))
out = {'source': 'R6/c1-n4/research/candidate017_dual_residual_replay/verification/result.json, mode_001.json, '
                 'mode_003.json (N4-425); fields copied verbatim',
       'result_sha256': sh(V + 'result.json'), 'result_utc': R['utc'], 'raw_sha256': R['raw_sha256'],
       'H_lower_square_exact': R['H_lower_square_exact'], 'H_strict_lower_exact': R['H_strict_lower_exact'],
       'complete_H_upper': R['complete_H_upper'],
       'complete_E2_and_017_less_than007': R['complete_E2_and_017_less_than007'],
       'modes': [{'n': m['n'], 'sha256': m['sha256'], 'quotient_strict_lower_exact': m['quotient_strict_lower_exact'],
                  'independent_hres': m['independent_hres']} for m in R['modes']],
       'residual': {}}
for f, n in (('mode_001.json', 1), ('mode_003.json', 3)):
    M = json.load(open(V + f))
    assert sh(V + f) == [m for m in R['modes'] if m['n'] == n][0]['sha256']
    rt = M['residual_trial']
    out['residual'][str(n)] = {
        'record_sha256': sh(V + f), 'dual_quotient_strict_lower_exact': M['dual_quotient_strict_lower_exact'],
        'H_mode_strict_lower_exact': rt['H_mode_strict_lower_exact'],
        'H_mode_strict_upper_exact': rt['H_mode_strict_upper_exact'],
        'gradient_ball_head': rt['gradient_ball'][0][:40] if isinstance(rt['gradient_ball'], list)
        else str(rt['gradient_ball'])[:40],
        'residual_ball_text': rt['residual_ball']}
json.dump(out, open(dest, 'w'), indent=1)
print(sh(dest), dest)
