from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import os,resource,sys,json,hashlib,time
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
if os.getpriority(os.PRIO_PROCESS,0)!=19 or sys.flags.optimize:raise RuntimeError('nice19 unoptimized')
from dyadic_root220 import Field as Root,I,B
import root220_replay_arithmetic as Other
from interval_residual221 import Field
r=Path('research/interval_residual221');paths=set();checks=[]
def sha(p):p=Path(p).resolve();paths.add(p);return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(v,s):
 if not v:raise AssertionError(s)
 checks.append(s)
for p in [__file__,'code/dyadic_root220.py','code/root220_replay_arithmetic.py','code/interval_residual221.py',r/'SOURCE_GX_PROOF.md',r/'RUNNER_REVIEW_PROOF.md']:sha(p)
pp=Path('research/implicit_root220/verification/plan.json');sha(pp);plan=json.loads(pp.read_text());rows=[];start=time.monotonic()
for src in plan['sources']:
 ck(sha(src['input'])==src['input_sha256']and sha(src['source'])==src['source_sha256'],'source bytes '+src['name']);data=json.loads(Path(src['input']).read_text());ck(data['source_sha256']==src['source_sha256'],'JSONsource '+src['name']);a,b,c=Root(data),Other.Function(data),Field(data);raw={}
 for seg in src['raw_segments']:
  ck(sha(seg['path'])==seg['sha256'],'rawpin '+seg['path']);raw.update({v['index']:v for v in map(json.loads,Path(seg['path']).read_text().splitlines())})
 for idx in [0,32,168,230,333,422,506,591,808,1182]:
  v=raw[idx];x=F(v['coordinate_exact_dyadics'][0]);q=F(v['fields']['eta']);h=F(q.numerator*(1<<40)//q.denominator,1<<40);u=a.gx(x,h);w=b.gx(x,h);z=c.generating(x,I.of(h),n=1).c[1,0];ivs=[(F(u.lo,B),F(u.hi,B)),(F(w[0],Other.UNIT),F(w[1],Other.UNIT)),(F(z.lo,B),F(z.hi,B))]
  for i,j in [(0,1),(0,2),(1,2)]:ck(max(ivs[i][0],ivs[j][0])<=min(ivs[i][1],ivs[j][1]),'pair overlap '+str((src['name'],idx,i,j)))
  rows.append({'name':src['name'],'source_sha256':src['source_sha256'],'index':idx,'x':str(x),'eta':str(h),'intervals':[list(map(str,v))for v in ivs],'widths':[str(v[1]-v[0])for v in ivs]});print(datetime.now(timezone.utc).isoformat(),src['name'],idx,'PASS',flush=True)
now=datetime.now(timezone.utc).isoformat();out={'utc':now,'status':'PASS_ACTUAL_SOURCE_THREE_WAY_GX_DIAGNOSTIC','check_count':len(checks),'checks':checks,'rows':rows,'elapsed_seconds':time.monotonic()-start,'scope':'Finite overlap diagnostic at20dyadicpoints, not a root certificate or primitive residual proof.','hashes':{str(p):sha(p)for p in sorted(paths)}};(r/'verification/source_gx.json').write_text(json.dumps(out,indent=2)+'\n');print(now,out['status'],len(checks))
