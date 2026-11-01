"""Certified logarithms of the already independent exact prime table."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from collections import defaultdict
import json, time
from flint import arb, fmpq, ctx

root = Path('research/80_compatibility_size_criterion')
for name in ['sources', 'verification']:
    (root/name).mkdir(exist_ok=True)
start = time.monotonic()
ctx.prec = 640
summary = json.loads(Path('research/57_prime_table/verification/summary.json').read_text())
assert summary['all_complete'] and summary['completed_count'] == 122
rows, groups, hashes = [], defaultdict(list), {}
text = lambda x: x.str(32, radius=True)
for case in summary['checks']:
    src = Path(case['evidence'])
    raw = src.read_bytes()
    exact = json.loads(raw)
    p, a = case['p'], case['a']
    value = arb(fmpq(exact['kappa_exact']))
    assert value != 0 and p < 4*a < 3*p
    logvalue = abs(value).log()/arb(10).log()/p
    rows.append(dict(p=p, a=a, log10_abs_kappa_over_p=text(logvalue)))
    groups[p].append((a, logvalue))
    hashes[str(src)] = sha256(raw).hexdigest()
group_rows = []
for p, vals in groups.items():
    lo = min(vals, key=lambda x: float(x[1].mid()))
    hi = max(vals, key=lambda x: float(x[1].mid()))
    assert all(lo[1] < v for a, v in vals if a != lo[0])
    assert all(hi[1] > v for a, v in vals if a != hi[0])
    group_rows.append(dict(p=p, count=len(vals), mean=text(sum((v for a,v in vals),arb(0))/len(vals)),
                           minimum=text(lo[1]), minimum_a=lo[0], maximum=text(hi[1]), maximum_a=hi[0]))
allvals = [(r['p'], r['a'], arb(r['log10_abs_kappa_over_p'])) for r in rows]
lo = min(allvals, key=lambda x: float(x[2].mid()))
hi = max(allvals, key=lambda x: float(x[2].mid()))
assert all(lo[2] < v for p,a,v in allvals if (p,a) != lo[:2])
assert all(hi[2] > v for p,a,v in allvals if (p,a) != hi[:2])
result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
              count=len(rows), precision_bits=640, source_hashes=hashes, rows=rows, by_prime=group_rows,
              minimum=dict(p=lo[0],a=lo[1],value=text(lo[2])),
              maximum=dict(p=hi[0],a=hi[1],value=text(hi[2])),
              actual_elapsed_s=time.monotonic()-start)
(root/'verification/kappa_sizes.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'sources/kappa_size_audit.py.txt').write_bytes(Path(__file__).read_bytes())
print(json.dumps({k:result[k] for k in ['checked_at_utc','count','minimum','maximum','by_prime','actual_elapsed_s']},indent=2))
