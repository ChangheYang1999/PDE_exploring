"""Recheck saved directed response discrepancies and collect the finite admission."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction
import gzip, json, sys
sys.dont_write_bytecode = True
from flint import arb, ctx
from gmpy2 import mpq
from pure_cartesian_ball import ball
from period_polar_prefix_replay import unpack
ROOT = Path('research/264_floating_response_accuracy')
def ref(p): return dict(path=str(p), sha256=sha256(p.read_bytes()).hexdigest())
def rat(x): return ball(mpq(str(x)))
def same(r): assert ref(Path(r['path'])) == r
ctx.prec = 768
path = ROOT/'verification/checks.json.gz'
d = json.loads(gzip.decompress(path.read_bytes()))
assert d['all_reference_checks_pass'] and d['bits'] == 768
assert len(d['results']) == 24
rows=[]
for r in d['results']:
    same(r['source']); same(r['prefix'])
    errors = [[], [], []]
    for item in r['rows']:
        v,w=unpack(item['exact_response']),unpack(item['binary_response'])
        assert not v.contains(0) and not w.contains(0)
        p=rat(item['printed'])
        vals=[abs((p-v)/v),abs((p-w)/w),abs((w-v)/v)]
        for j,(value,key) in enumerate(zip(vals,['relative_exact_discrepancy','relative_binary_discrepancy','relative_root_rounding'])):
            assert value.overlaps(arb(item[key]))
            assert value < rat(Fraction(61,10**13) if j<2 else Fraction(134,10**14))
            errors[j].append(value)
    assert len(r['rows']) == r['count'] == r['last_index']-r['first_index']+1
    maxima=[max(x,key=lambda v:float(v.mid())) for x in errors]
    rows.append(dict(source=Path(r['source']['path']).name,Q=r['Q'],root=r['root_index'],completed=r['completed'],first=r['first_index'],last=r['last_index'],count=r['count'],maxima=[x.str(18,radius=True) for x in maxima]))
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
check=dict(checked_at_utc=now,all_checks_pass=True,evidence=ref(path),rows=rows,total_responses=sum(x['count'] for x in rows),strict_relative_bounds={'exact_root':'61/10000000000000','binary_input':'61/10000000000000','root_rounding':'134/100000000000000'},scope='Finite saved responses only; strict bounds independently reassembled from the stored directed enclosures.')
(ROOT/'verification/discrepancy_recheck.json').write_text(json.dumps(check,indent=2)+'\n')
lines=['# Finite tuning-response accuracy','',f'Checked {now}. The tables concern 915 saved response values. They do not bound errors in the later full coefficient arrays.','',
'Every saved response has relative discrepancy below 6.1e-12 from its exact algebraic-root value. Replacing the exact root by the producer\'s binary64 input changes these responses by less than 1.34e-12. The output format prints thirteen significant digits, which limits the comparison even when the internal arithmetic is more accurate.','',
'| Output | k range | Completed | Largest relative discrepancy: exact root | Binary input | Root rounding effect |', '|---|---|---|---:|---:|---:|']
for x in rows:
    ms=[float(arb(t).mid()) for t in x['maxima']]
    lines.append(f"| {x['source']} | {x['first']}..{x['last']} | {x['completed']} | {ms[0]:.4e} | {ms[1]:.4e} | {ms[2]:.4e} |")
lines+=['','The response calculation uses 768-bit directed arithmetic, 168 overlaps with independently replayed prefix responses, and 96 full/compact cross-checks. Its actual arithmetic time was 250.47073 seconds. The two baseline root-1 outputs stopped early; their rescaled runs completed. Extended precision starts from the same binary64 root and does not correct that input error.']
(ROOT/'RESPONSE_TABLE.md').write_text('\n'.join(lines)+'\n')
(ROOT/'sources/collect_floating_response_admission.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps({k:v for k,v in check.items() if k!='rows'},indent=2))
