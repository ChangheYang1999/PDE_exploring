"""Exact fmpq running-maximum union, with explicit current topic152 input pins."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import fmpq
import json,gzip,hashlib,time
B=Path(__file__).resolve().parents[3];D=B/'research/literal_derivative_cell_union';S=B/'research/weighted_derivative_scalar_norms'
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def q(x):
 n,d=x.as_integer_ratio();return fmpq(n,d)
def fromstr(s):
 x=F(s);return fmpq(x.numerator,x.denominator)
def union(rows):
 ordered=sorted(rows,key=lambda x:x[0]);need(ordered and all(a<b for a,b in ordered),'nonempty intervals');components=[];gaps=[];left,right=ordered[0]
 for a,b in ordered[1:]:
  if a<=right:right=max(right,b)
  else:components.append([str(left),str(right)]);gaps.append([str(right),str(a)]);left,right=a,b
 components.append([str(left),str(right)])
 return {'intervals':len(rows),'strictly_increasing_starts':all(a[0]<b[0] for a,b in zip(rows,rows[1:])),'strictly_increasing_ends':all(a[1]<b[1] for a,b in zip(rows,rows[1:])),'hull':[str(ordered[0][0]),str(max(b for a,b in ordered))],'components':components,'gaps':gaps,'gap_count':len(gaps),'union_components':len(components),'missing_log_length':str(sum((fromstr(b)-fromstr(a) for a,b in gaps),fmpq(0))),'max_gap':str(max([fmpq(0)]+[fromstr(b)-fromstr(a) for a,b in gaps]))}
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();v=json.loads((S/'evidence/verdict.json').read_text());need(sha(S/'evidence/verdict.json')=='536c7886967dfbe139a8bcb8bb5827e5165fd6100e3d5a3f095c1e1bfb5ae742','topic152 fixed verdict');pins=dict(v['files']);pins[str((S/'evidence/verdict.json').relative_to(B))]=sha(S/'evidence/verdict.json')
for n,h in pins.items():need(sha(B/n)==h,'actual inherited pinned source')
regions={};allrows=[];checks=0
with gzip.open(S/'data_exact/rows.jsonl.gz','rt') as f:
 for reg in ['inner','middle','outer']:
  rows=[]
  for j,r in enumerate(json.loads((S/'sources'/('derivative_'+reg+'.json')).read_text())['rows']):
   x=json.loads(next(f));need(x['region']==reg and x['index']==r['ci']==j,'ordered source row');a,h=q(r['t_a']),q(r['h']);need(a==fromstr(x['exact']['t_a']) and h==fromstr(x['exact']['h']) and h>0,'exact row export checked');rows.append((a,a+h));checks+=2
  regions[reg]=union(rows);allrows+=rows
 need(next(f,None) is None,'complete exact input export')
regions['all']=union(allrows)
for n,r in regions.items():
 need(r['strictly_increasing_starts'] and r['strictly_increasing_ends'],'all actual start and end monotonicities')
for p in [Path(__file__),D/'PROOF.md']:pins[str(p.relative_to(B))]=sha(p)
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_RUNNING_MAXIMUM_UNION_ONLY','source_scalar_checks':checks,'regions':regions,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'Literal saved closed intervals only. Actual gap components and missing log-length, no bounds on physical residual in gaps or infinite tails.'}
with (D/'evidence/merge.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'seconds':out['seconds'],'source_scalar_checks':checks,'regions':{n:{k:v for k,v in r.items() if k not in ['components','gaps']} for n,r in regions.items()}},indent=2))
