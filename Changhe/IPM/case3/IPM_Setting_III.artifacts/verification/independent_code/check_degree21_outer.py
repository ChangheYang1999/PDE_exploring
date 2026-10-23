"""Exact bound-plus-one fixed-degree Sylvester checker, all our own determinants."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,resource,time,traceback,sys
from flint import fmpz,fmpq
from exact_degree21 import decode,degree,coef,univ
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3));sys.set_int_max_str_digits(1000000)
R=Path('research/degree21_grouped_moment_obstruction');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat();checks=[];details=[]
def ck(name,ok,e=None):
 checks.append(dict(name=name,passed=bool(ok),evidence=e))
 if not ok:raise AssertionError((name,e))
def horner(c,z):
 v=fmpz(0)
 for t in reversed(c):v=v*z+fmpz(t)
 return v
def special(p,i,N,z):return [horner(univ(coef(p,i,j)),z)for j in range(N,-1,-1)]
def matrix(a,b):
 m=len(a)-1;n=len(b)-1;return [[fmpz(0)]*k+a+[fmpz(0)]*(n-1-k)for k in range(n)]+[[fmpz(0)]*k+b+[fmpz(0)]*(m-1-k)for k in range(m)]
def det(a):
 a=[r[:]for r in a];sign=1;old=fmpz(1);divs=0;swaps=0
 for k in range(len(a)-1):
  piv=next((i for i in range(k,len(a))if a[i][k]),None)
  if piv is None:return fmpz(0),divs,swaps
  if piv!=k:a[k],a[piv]=a[piv],a[k];sign=-sign;swaps+=1
  d=a[k][k]
  for i in range(k+1,len(a)):
   aik=a[i][k]
   for j in range(k+1,len(a)):
    q,r=divmod(a[i][j]*d-aik*a[k][j],old)
    if r:raise ArithmeticError('integer Bareiss division nonexact')
    a[i][j]=q;divs+=1
   a[i][k]=fmpz(0)
  old=d
 return sign*a[-1][-1],divs,swaps
def gauss(a):
 a=[[fmpq(v)for v in r]for r in a];out=fmpq(1)
 for k in range(len(a)):
  piv=next((i for i in range(k,len(a))if a[i][k]),None)
  if piv is None:return fmpq(0)
  if piv!=k:a[k],a[piv]=a[piv],a[k];out=-out
  d=a[k][k];out*=d
  for i in range(k+1,len(a)):
   ratio=a[i][k]/d
   for j in range(k+1,len(a)):a[i][j]-=ratio*a[k][j]
   a[i][k]=fmpq(0)
 return out
start=utc();input_hash=sha(V/'RECONSTRUCTION.json')
def save(status):
 out=dict(status=status,started_utc=start,updated_utc=utc(),count=len(checks),checks=checks,cases=details,reconstruction_sha256=input_hash,driver_sha256=sha(__file__),library_sha256=sha('independent_code/exact_degree21.py'),proof_sha256=sha(R/'OUTER_DETERMINANT_PROOF.md'))
 (V/'OUTER_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
try:
 rec=json.loads((V/'RECONSTRUCTION.json').read_text());ck('reconstruction complete',rec['status']=='PASS' and all(q['passed']for q in rec['checks']));ck('reconstruction library',rec['library_sha256']==sha('independent_code/exact_degree21.py'));ck('reconstruction driver',rec['driver_sha256']==sha('independent_code/check_degree21_reconstruction.py'))
 for no,j in enumerate(rec['jobs']):
  f,g=decode(j['f']),decode(j['g']);i=j['var'];m,n=degree(f,i),degree(g,i);a,b=degree(f,2),degree(g,2);B=n*a+m*b;co=univ(decode(j['resultant']));name=j['name'];ck(name+' target degree bound',len(co)-1<=B and co[-1]!=0);info=dict(name=name,degrees=[m,n,a,b],bound=B,target_degree=len(co)-1,started_utc=utc(),samples=0);details.append(info);save('RUNNING');print('START',no,name,'bound',B,'matrix',m+n,utc(),flush=True)
  C=None;normalization_point=None
  # eta 23 is already strictly positive for sign-certified targets. Mixed-sign
  # targets may vanish at isolated nodes, so do not assume nonzero here.
  for z in range(23,23+B+1):
   mat=matrix(special(f,i,m,z),special(g,i,n,z));value,nd,ns=det(mat);q=horner(co,z)
   if C is None and q and value:C=fmpq(value,q);normalization_point=z;info['constant']=str(C);info['normalization_point']=z
   if C is None:ck(name+' preliminary both zero eta='+str(z),not q and not value)
   else:ck(name+' exact eta='+str(z),fmpq(value)==C*q,dict(divisions=nd,swaps=ns))
   info['samples']+=1
   if z in [23,24,25]:ck(name+' Gaussian eta='+str(z),gauss(mat)==value)
   if (z-23)%25==0:save('RUNNING');print('POINT',no,name,z,'checks',len(checks),utc(),flush=True)
  ck(name+' nonzero constant and full degree identity',C is not None and C!=0 and info['samples']==B+1)
  info['finished_utc']=utc();save('RUNNING');print('DONE',name,utc(),flush=True)
 ck('input unchanged',input_hash==sha(V/'RECONSTRUCTION.json'));save('PASS');print('PASS',len(checks),utc(),flush=True)
except BaseException:
 save('FAIL');(V/'outer_traceback.txt').write_text(traceback.format_exc());raise
