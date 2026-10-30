"""Compare the complete leading prefix with the independently produced table."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime, timezone
from math import isclose
import json
import time
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/generator_sector_audit'
NAME = 'C1-N1-010-d2w-j7-x3bal-legqs'

def H(p):
    return sha256(p.read_bytes()).hexdigest()

start = time.monotonic()
ctx.prec = 1024
own_path = BASE / f'verification/{NAME}_direct.json'
table_path = ROOT / f'research/candidate_audits/data/{NAME}/sector_table.json'
own = json.loads(own_path.read_text())
table = json.loads(table_path.read_text())
assert H(table_path) == own['snapshot_hashes']['sector_table.json']
assert own['c_exact'] == table['cl_exact']
summary = own['sector_summary']
assert summary['all_forbidden_zero'] and summary['forbidden_prefix_complete']
assert summary['leading_certified_by_complete_prefix']
lead = Q(summary['leading_exponent'])
assert Q(summary['omitted_exponent_upper_bound']) < lead
peer = {Q(row['exponent_exact']): row for row in table['rows']}
matched = []
for row in own['sectors']:
    exponent = Q(row['exponent'])
    if exponent < lead:
        continue
    target = peer[exponent]
    assert row['exact_zero'] == (target['status'] == 'EXACT-ZERO')
    if not row['exact_zero']:
        assert exponent == lead
        # Published decimal entries are diagnostics, not interval certificates.
        assert isclose(float(arb(row['full_circle_norm']).mid()), target['full_circle_L2'], rel_tol=2e-14)
        assert set(row['sine_coefficients']) == set(target['coefficients_float'])
        for key, value in row['sine_coefficients'].items():
            assert isclose(float(Q(value)), target['coefficients_float'][key], rel_tol=2e-14, abs_tol=1e-25)
    matched.append({'exponent': str(exponent), 'exact_zero': row['exact_zero']})
assert len(matched) == 12 and sum(row['exact_zero'] for row in matched) == 11
out = {
    'utc': datetime.now(timezone.utc).isoformat(), 'candidate': NAME,
    'complete_leading_prefix_comparisons': matched,
    'leading_harmonic_coefficients_compared': len(next(row for row in own['sectors'] if Q(row['exponent']) == lead)['sine_coefficients']),
    'inputs': {str(p.relative_to(ROOT)): H(p) for p in [own_path, table_path, Path(__file__), BASE/'PROOF.md', BASE/'PROOF_CANDIDATES.md']},
    'elapsed_seconds': time.monotonic() - start,
    'verdict': 'CONFIRMED exact source and complete leading-prefix structure; published decimal coefficients agree diagnostically. Point obstruction remains OPEN peer.'
}
dest = BASE / 'verification/candidate010_table_comparison.json'
assert not dest.exists()
dest.write_text(json.dumps(out, indent=2) + '\n')
print(out['verdict'], len(matched), flush=True)
