"""Sequential finite recount of a frozen selected set of admitted ordinary roots."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
import json,subprocess,sys,time,os
R=Path(__file__).resolve().parents[3];D=Path(__file__).resolve().parents[1]
assert Path.cwd()==R and os.sched_getaffinity(0)=={50}and os.getpriority(os.PRIO_PROCESS,0)>=19
assert all(os.environ.get(x)=='1'for x in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'])
def h(p):return sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
sel=D/'verification/batch_selection_v01.json';m=read(sel)
for n,v in m['files'].items():assert h(R/n)==v
assert [r['index']for r in m['roots']]==[i for i in range(61)if i!=34]
start=datetime.now(timezone.utc);tick=time.monotonic();rows=[]
for row in m['roots']:
 assert h(R/row['publication'])==row['publication_sha256']
 out=R/row['output']
 if row['existing_sha256']is not None:assert h(out)==row['existing_sha256']
 else:
  assert not out.exists()
  subprocess.run([sys.executable,'-B',str((D/'code/check_v01.py').relative_to(R)),'--publication',row['publication'],'--output',row['output']],check=True,timeout=60)
 r=read(out);assert r['status']=='CONDITIONAL_EXACT_MATRIX_MARGIN'and r['index']==row['index']
 assert r['files'][row['publication']]==row['publication_sha256']
 for n,v in m['method_files'].items():assert r['files'][n]==v
 rows.append(dict(index=row['index'],result=row['output'],sha256=h(out),lower=r['outward_lower_exact'],combined_lower=str(max(Q(3,5),Q(r['outward_lower_exact']))),checks=r['checks'],seconds=r['elapsed_seconds']))
for n,v in m['files'].items():assert h(R/n)==v
for row in rows:assert h(R/row['result'])==row['sha256']
targets=['17/25','69/100','7/10','704017099351/1000000000000','141/200','71/100']
def union(js):
 ans=[]
 for j in js:
  lo,hi=Q(j,128),Q(j+1,128)
  if ans and lo<=ans[-1][1]:ans[-1][1]=max(hi,ans[-1][1])
  else:ans.append([lo,hi])
 return [[str(lo),str(hi)]for lo,hi in ans]
worst=min(rows,key=lambda r:Q(r['combined_lower']))
z=dict(status='CONDITIONAL_EXACT_MATRIX_BATCH',started_utc=start.isoformat(),finished_utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-tick,roots=rows,selection_sha256=h(sel),minimum_index=worst['index'],minimum_lower=worst['combined_lower'],selected_t_union=union([r['index']for r in rows]),targets={t:dict(indices=[r['index']for r in rows if Q(r['combined_lower'])>=Q(t)],t_union=union([r['index']for r in rows if Q(r['combined_lower'])>=Q(t)]))for t in targets},scope='Conditional finite union of authenticated admitted intervals and new exact recounts. Independent review required for improved constants; root34 and all indices above60 excluded. No global bound.')
with (D/'verification/batch_standard_000_060_v01.json').open('x')as f:json.dump(z,f,indent=2);f.write('\n')
print('BATCH_MATRIX',len(rows),'MIN',worst['index'],worst['combined_lower'],'SECONDS',z['seconds'],flush=True)
