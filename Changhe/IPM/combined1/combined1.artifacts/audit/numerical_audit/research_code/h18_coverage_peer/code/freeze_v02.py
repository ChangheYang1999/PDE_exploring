"""Copy explicitly listed finite evidence before own arithmetic; no peer execution."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,os,gzip
R=Path(__file__).resolve().parents[3];B=R/'research/h18_coverage_peer'
P=R.parent/'c1-t4/research/h18_coverage_audit';T=R.parent/'c1-t2'
def digest(x):return sha256(x).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
assert not (B/'verification/PREPARE.json').exists()
items={}
def add(original,local,expected=None):
 original=Path(original);raw=original.read_bytes();h=digest(raw)
 if expected:assert expected==h,(original,expected,h)
 if local in items:assert items[local]['sha256']==h;return
 items[local]={'original':str(original),'local':local,'sha256':h,'bytes':len(raw),'raw':raw}
for name in ['PROOF.md','data/manifest.json','data/coverage.json','data/families.json','data/registry.json','code/check.py','verification/result.json','verification/checks.json']:
 add(P/name,'source/T4/'+name)
manifest=json.loads((P/'data/manifest.json').read_text())
for e in manifest:add(P/e['local'],'source/T4/'+e['local'],e['sha256'])
for name in ['reviews/REVIEW_T4_459.md','artifacts/arith/review_t4_459.py','artifacts/data/review_t4_459_results.json','artifacts/logs/review_t4_459.log']:
 add(T/name,'source/T2/'+name)
r=json.loads((T/'artifacts/data/review_t4_459_results.json').read_text())
for name,h in r['inputs'].items():add(R.parent/name,'source/T2_inputs/'+name,h)
size=sum(e['bytes'] for e in items.values());assert size<60_000_000,size
for local,e in items.items():
 raw=e.pop('raw');e['gzip']=len(raw)>65536;e['storage']=local+('.gz' if e['gzip'] else '');data=gzip.compress(raw,compresslevel=6,mtime=0) if e['gzip'] else raw;e['stored_sha256']=digest(data);e['stored_bytes']=len(data);e['payload']=data
stored_size=sum(e['stored_bytes'] for e in items.values());assert stored_size<12_000_000,stored_size
for local,e in items.items():
 out=B/e['storage'];out.parent.mkdir(parents=True,exist_ok=True);assert not out.exists();out.write_bytes(e.pop('payload'))
rows=list(items.values());(B/'source/MANIFEST.json').write_text(json.dumps(rows,indent=2)+'\n')
prep={'utc':now(),'proof_sha256':digest((B/'PROOF.md').read_bytes()),'checker_exists':(B/'code/check.py').exists(),'manifest_sha256':digest((B/'source/MANIFEST.json').read_bytes()),'files':len(rows),'decoded_bytes':size,'stored_bytes':stored_size,'storage_proof_sha256':digest((B/'STORAGE_PROOF_v02.md').read_bytes()),'first_freezer_sha256':digest((B/'code/freeze.py').read_bytes()),'peer_executed':False,'freeze_code_sha256':digest(Path(__file__).read_bytes())}
assert not prep['checker_exists'];(B/'verification/PREPARE.json').write_text(json.dumps(prep,indent=2)+'\n');print(json.dumps(prep))
