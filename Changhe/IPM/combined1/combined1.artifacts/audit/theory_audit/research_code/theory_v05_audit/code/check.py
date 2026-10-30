"""Exact audit of v05 arithmetic and counterexample calculations."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib
import json
import time
from flint import arb, ctx

B = Path(__file__).resolve().parents[1]
ctx.prec = 512
start = time.monotonic()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
a = lambda x: arb(Q(x).numerator) / Q(x).denominator
rows = []
allowed = {'d2','Mpen2','005','006','007','008','009','010','012','013','014','015'}
for line in (B/'source/theory_v05.md').read_text().splitlines():
    if not line.startswith('| '):
        continue
    cols = [x.strip() for x in line.split('|')[1:-1]]
    if len(cols) != 6 or cols[0] not in allowed:
        continue
    floor = Q(cols[1].split()[0])
    ratios = []
    for label, col, den in zip(['TB-sharp','sharpw','graded'], cols[2:5],
                              [Q('3.7930e-6'), Q('2.8496e-6'), Q(25,54684)]):
        claim, actual = Q(col), floor/den
        assert claim < actual, (cols[0], label, claim, actual)
        ratios.append({'budget':label, 'budget_exact':str(den),
                       'claimed_factor':str(claim), 'exact_lower_ratio':str(actual),
                       'strictly_conservative':True})
    rows.append({'candidate':cols[0], 'distance_lower_exact':str(floor), 'ratios':ratios})
assert len(rows) == 12 and {r['candidate'] for r in rows} == allowed
# The complete finite polynomial (1-v)^2(1+v) = 1-v-v^2+v^3.
beta_example = sum(Q(c)/(Q(3,2)+j) for j,c in enumerate([1,-1,-1,1]))
assert beta_example == Q(64,315)
assert Q(1,2) < 1 and 3**2 + Q(1,2)**2 == Q(37,4) > 1
old, ceiling, upward = Q('0.00045717'), Q(25,54684), Q('0.000457173')
assert old < ceiling < upward
fine = arb(50)/(651*arb(28248).sqrt())
assert fine < a(old)
assert 54684*45717 == 2499988428 < 2500000000
assert 54684*457173 == 25000048332 > 25000000000
out = {
    'utc':datetime.now(timezone.utc).isoformat(),
    'source_sha256':sha(B/'source/theory_v05.md'),
    'proof_sha256':sha(B/'PROOF.md'), 'code_sha256':sha(Path(__file__)),
    'candidate_rows':rows, 'all_36_ratios_strictly_conservative':True,
    'complete_beta_example_exact':str(beta_example),
    'heldout_decreases_while_actual_distance_increases':True,
    'old_decimal_strictly_below_rational_ceiling':True,
    'replacement_decimal_strictly_above_rational_ceiling':True,
    'finer_graded_ceiling':fine.str(90),
    'finer_graded_ceiling_below_old_decimal':True,
    'elapsed_seconds':time.monotonic()-start,
}
with (B/'verification/result.json').open('x') as stream:
    json.dump(out,stream,indent=2)
    stream.write('\n')
print(json.dumps({k:v for k,v in out.items() if k != 'candidate_rows'},indent=2))
