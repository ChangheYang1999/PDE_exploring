from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import hashlib, json
ROOT = Path(__file__).resolve().parents[1]
d = json.loads((ROOT / 'evidence/check.json').read_text())
assert d['status'] == 'PASS'
assert d['proof_sha256'] == hashlib.sha256((ROOT / 'PROOF.md').read_bytes()).hexdigest()
assert d['code_sha256'] == hashlib.sha256((ROOT / 'code/check.py').read_bytes()).hexdigest()
source = ROOT.parents[2] / 'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
assert d['original_sha256'] == hashlib.sha256(source.read_bytes()).hexdigest()
rows = {F(x['T']): x for x in d['rows']}
bounds = {F(18): ('588050.16', '591744.16'), F(20): ('203443.34', '203445.56'), F(25): ('14192.84666678', '14192.84666680'), F(30): ('990.0012675088110412', '990.0012675088110415')}
for t, (lo, hi) in bounds.items():
    row = rows[t]['full_Y']
    assert F(row['energy_lower']['lower_exact']) > F(lo)
    assert F(row['energy_upper']['upper_exact']) < F(hi)
    assert F(row['relative_error_bound']['lower_exact']) >= 0
    assert F(row['relative_error_bound']['upper_exact']) < 1
k = F(1615536043799051, 9007199254740992)
pairs = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)]
a = [k-3-j*(1-k)-2*l for j,l in pairs]
expected = set(a[1:]) | {e+f+2 for e in a for f in a}
assert set(map(F, d['regular_exponents'])) == expected
assert max(expected) == 2*k-4
assert all(2*e+F(27,4)<0 for e in expected)
assert (k-1)-6 == -4+(k-3) == k-7
out = {'date': datetime.now(timezone.utc).isoformat(), 'status': 'PASS', 'check': 'Exact rational output bounds, original/proof/code hashes, independent exponent set and error rates', 'bounds': {str(t): list(v) for t,v in bounds.items()}}
(ROOT / 'evidence/audit.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out))
