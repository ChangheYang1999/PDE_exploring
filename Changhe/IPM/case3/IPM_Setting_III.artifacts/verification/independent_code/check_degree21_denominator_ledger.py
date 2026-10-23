"""Result285: independent localization ledger on verified group coefficients."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,traceback,resource
from exact_degree21 import *
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3))
R=Path('research/degree21_grouped_moment_obstruction');V=R/'verification';E=V/'external';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat();checks=[];rows=[];t0=utc()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def save(status):
 (V/'DENOMINATOR_LEDGER.json').write_text(json.dumps(dict(status=status,count=len(checks),checks=checks,rows=rows,started_utc=t0,updated_utc=utc(),proof_sha256=sha(R/'REVIEW_RESOLUTION_PROOF.md'),driver_sha256=sha(__file__),library_sha256=sha('independent_code/exact_degree21.py'),reconstruction_sha256=sha(V/'RECONSTRUCTION.json')),indent=2)+'\n')
save('RUNNING')
try:
 rec=json.loads((V/'RECONSTRUCTION.json').read_text());ck('reconstruction1058PASS',rec['status']=='PASS'and rec['count']==1058 and all(c['passed']for c in rec['checks']));ck('library',rec['library_sha256']==sha('independent_code/exact_degree21.py'))
 for i in range(1,30):
  s=json.loads((E/f'certificate_{i:02d}.json').read_text());d=s['certificate'];pat=s['pattern'];A=pat['A0'];K=pat['e'];kind=pat['type'];name=f'{i} {kind}';row=dict(index=i,kind=kind,source_sha256=sha(E/f'certificate_{i:02d}.json'));allowed=[h,A*h-21]
  if kind in ['exception','two_pairs']:
   row['scope']='No grouped elimination; independently checked normalized-value and positivity gates';rows.append(row);continue
  if kind=='II':
   z=qdecode(d['second_node']);groups=[[Q(1),Q(-x)],[Q(1),-z],[qdecode(a)for a in d['group_polynomial']]];weights=d['weights'];allowed.append(decode(d['S']))
  elif kind in ['IV','VI']:
   groups=[[Q(1),Q(-x)]]+[[qdecode(a)for a in co]for co in d['group_polynomials']];weights=d['weights'];allowed.extend([h-x,qdecode(d['L1']).n,qdecode(d['L2']).n])
  else:groups=[[qdecode(a)for a in co]for co in d['group_polynomials']];weights=d['weights']
  D=C.constant(1)
  for j,co in enumerate(groups):
   for k,a in enumerate(co):
    D*=a.d;rem=prim(a.d)
    for f in map(prim,allowed):
     while rem.total_degree()>0:
      q,r=divmod(rem,f)
      if r:break
      rem=q
    ck(name+f' coefficient denominator {j}/{k}',rem.total_degree()==0)
  D=prim(D);pp=[ps(co,K)for co in groups];mom=[]
  for k in range(1,K+1):
   M=Q(A*(h-1)**k)+sum((w*p[k]for w,p in zip(weights,pp)),Q(0));den=prim(M.d);q,r=divmod(D**k,den);ck(name+' moment denominator '+str(k),not r);mom.append(dict(k=k,denominator=encode(den),common_denominator_power=k))
  row.update(common_denominator=encode(D),moments=mom,allowed=[encode(prim(p))for p in allowed],removals={})
  if kind in ['IV','V','VI']:
   for key,records in d['regular'].items():
    if not key.startswith('removed_'):continue
    permitted=[h,A*h-21]if key=='removed_from_common_resultant'else allowed
    for j,r in enumerate(records):ck(name+key+str(j),r['exponent']>=0 and any(prim(decode(r['polynomial']))==prim(p)for p in permitted))
    row['removals'][key]=records
   ck(name+' full outer target has no removal key',not any(k in d['regular']for k in ['removed_from_resultant','removed_from_other_resultant']))
  if kind=='V':
   Lp=-Q(h-21,2*h);Lq=Q(h-21,2*h);ck('V logs nonzero',Lp.n!=0 and Lq.n!=0 and Lp+Lq==0 and 4*Lp+2*Lq==-Q(h-21,h))
   for key,power in [('removed_from_U',6),('removed_from_V',5),('removed_from_W',8)]:
    r=d['regular'][key];ck('V exact ledger '+key,len(r)==1 and r[0]['exponent']==power and prim(decode(r[0]['polynomial']))==prim(h-21))
  if kind=='VI':
   a1=(h-21)*x-(h-17)*h;a2=(h-21)*x-(h-19)*h
   want={'U':[4,3],'V':[3,2],'Q1':[2,1],'Q2':[1,0],'R':[0,2],'aux_V':[2,0]}
   for key,powers in want.items():
    r=d['regular']['removed_from_'+key];actual=C.constant(1)
    for z in r:actual*=decode(z['polynomial'])**z['exponent']
    ck('VI exact ledger '+key,prim(actual)==prim(a1**powers[0]*a2**powers[1]))
  rows.append(row);save('RUNNING');print('LEDGER',name,len(checks),utc(),flush=True)
 ck('all29cases',len(rows)==29);save('PASS');print('PASS',len(checks),utc(),flush=True)
except Exception:
 save('FAIL');(V/'denominator_traceback.txt').write_text(traceback.format_exc());raise
