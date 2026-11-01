"""Small checkpoint roundtrip and production-log provenance reproduction."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
sys.path.insert(0,'../a4-num/code')
from logff import LogFarField, make_ring
BASE=Path('research/190_reset_provenance_roundtrip')
start=time.monotonic()
obj=LogFarField(make_ring('arb',512),2,3,['1'])
obj.radii_reset_at=1;obj.perturbed_seed=17;obj._stats(1)
before=dict(radii_reset_at=obj.radii_reset_at,perturbed_seed=obj.perturbed_seed,midpoint_only=obj.stats[1]['midpoint_only'])
path=BASE/'verification/roundtrip.pkl';obj.save(str(path));other=LogFarField.load(str(path));other._stats(1)
after=dict(radii_reset_at=getattr(other,'radii_reset_at',None),perturbed_seed=getattr(other,'perturbed_seed',None),midpoint_only=other.stats[1]['midpoint_only'])
assert before['midpoint_only'] is True and after['midpoint_only'] is False and after['radii_reset_at'] is None and after['perturbed_seed'] is None
log=Path('../a4-num/logs/log_sin1_c3_from329.jsonl');rows=[]
for line in log.read_text().splitlines():
 d=json.loads(line)
 if 'tag' in d or d.get('n',0)>350:rows.append(d)
assert any(x.get('resumed_from')==350 and x.get('radii_reset_at') is None for x in rows)
assert any(x.get('n')==351 and x.get('midpoint_only') is False for x in rows)
(BASE/'sources/production_log_excerpt.json').write_text(json.dumps(rows,indent=2)+'\n')
sources={}
for name in ['logff.py','ffcore.py']:
 raw=Path('../a4-num/code',name).read_bytes();(BASE/'sources'/name).write_bytes(raw);sources[name]=sha256(raw).hexdigest()
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),defect_reproduced=True,before=before,after=after,source_sha256=sources,production_rows=len(rows),actual_elapsed_s=time.monotonic()-start)
(BASE/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n');(BASE/'sources/check_reset_provenance.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(result),flush=True)
