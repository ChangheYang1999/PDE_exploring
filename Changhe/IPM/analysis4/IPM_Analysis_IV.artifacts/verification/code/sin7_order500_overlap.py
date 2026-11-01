"""Compare the new sin7 prefix with the completed old run, allowing final tuning."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import gzip,json,pickle,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
from stream_precision_audit import unpack
ROOT=Path('research/293_sin7_order500');OUT=ROOT/'verification'
def read(p):
 p=Path(p);r=p.read_bytes();return json.loads(gzip.decompress(r) if p.suffix=='.gz' else r)
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
start=time.monotonic();ctx.prec=2048
prior=Path('research/271_single_harmonic_finite_audit/verification/sin7/checks.json.gz');new=OUT/'sin7/checks.json.gz'
a,b=read(prior),read(new);assert a['all_checks_pass'] and b['all_checks_pass'] and a['maximum_order']==300 and b['maximum_order']==500
states=[]
for data in [a,b]:
 raw=Path(data['source']['path']).read_bytes();assert sha256(raw).hexdigest()==data['source']['sha256'];states.append(pickle.loads(raw));del raw
counts={'f':0,'g':0};excluded=[]
for field in ['f','g']:
 for n in range(1,301):
  old,newer=states[0][field][n],states[1][field][n];assert len(old)==len(newer)
  for j,(x,y) in enumerate(zip(old,newer)):
   if field=='g' and n==300 and j==119:excluded.append((n,j,x,y));continue
   assert x==y,('packed prefix mismatch',field,n,j)
   counts[field]+=1
assert len(excluded)==1
n,j,x,y=excluded[0];old,newer=arb(*unpack(x)),arb(*unpack(y));assert old.is_zero()
h=read(b['harmonics']['path']);H=arb(h['H']['300']['str']);assert not H.contains(0) and newer.overlaps(H)
logs=[]
for data in [a,b]:
 p=Path(data['log']['path']);raw=p.read_bytes();assert sha256(raw).hexdigest()==data['log']['sha256']
 logs.append({r['n']:r['log10_l1'] for r in map(json.loads,raw.splitlines()) if 'n' in r and 'log10_l1' in r})
for n in range(1,301):assert logs[0][n]==logs[1][n],('printed prefix norm',n)
result=dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,through_order=300,packed_equalities=counts,printed_norm_equalities=300,excluded_final_free_harmonic=dict(n=300,j=119,frequency=238,old_zero=True,new_value=newer.str(40),recorded_H=H.str(40),overlaps=True),inputs=[ref(prior),ref(new)],source_checksums=[a['source'],b['source']],actual_elapsed_s=time.monotonic()-start,scope='Finite exact reproduction except the previously unset final harmonic, which is now tuned.')
(OUT/'overlap.json').write_text(json.dumps(result,indent=2)+'\n');(ROOT/'sources/sin7_order500_overlap.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(result),flush=True)
