"""Exact univariate resultant identities from formal-degree Sylvester matrices."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,gzip,resource,traceback,sys
from flint import fmpz,fmpq
from exact_degree21 import decode,degree,coef,univ,C,x,h
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3))
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(1000000)
R=Path('research/degree23_grouped_moment_obstruction');V=R/'verification';O=V/'outer';O.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()

def horner(co,z):
 out=fmpz(0)
 for q in reversed(co):out=out*z+fmpz(q)
 return out

def coeffs(p,i,N):return [univ(coef(p,i,k))for k in range(N,-1,-1)]
def matrix(a,b):
 m=len(a)-1;n=len(b)-1
 return [[fmpz(0)]*j+a+[fmpz(0)]*(n-j-1)for j in range(n)]+[[fmpz(0)]*j+b+[fmpz(0)]*(m-j-1)for j in range(m)]
def det(a):
 a=[r[:]for r in a];old=fmpz(1);sign=1;nd=0;ns=0
 for k in range(len(a)-1):
  pi=next((i for i in range(k,len(a))if a[i][k]),None)
  if pi is None:return fmpz(0),nd,ns
  if pi!=k:a[k],a[pi]=a[pi],a[k];sign=-sign;ns+=1
  pivot=a[k][k]
  for i in range(k+1,len(a)):
   aik=a[i][k]
   for j in range(k+1,len(a)):
    q,rem=divmod(a[i][j]*pivot-aik*a[k][j],old)
    if rem:raise ArithmeticError('nonexact integer Bareiss division')
    a[i][j]=q;nd+=1
   a[i][k]=fmpz(0)
  old=pivot
 return sign*a[-1][-1],nd,ns

def gauss(a):
 a=[[fmpq(v)for v in row]for row in a];out=fmpq(1)
 for k in range(len(a)):
  pi=next((i for i in range(k,len(a))if a[i][k]),None)
  if pi is None:return fmpq(0)
  if pi!=k:a[k],a[pi]=a[pi],a[k];out=-out
  pivot=a[k][k];out*=pivot
  for i in range(k+1,len(a)):
   ratio=a[i][k]/pivot
   for j in range(k+1,len(a)):a[i][j]-=ratio*a[k][j]
   a[i][k]=fmpq(0)
 return out

def packwrite(path,data):
 tmp=path.with_suffix('.tmp');tmp.write_bytes(gzip.compress((json.dumps(data,indent=1)+'\n').encode(),compresslevel=6,mtime=0));tmp.replace(path)

# Independent analytic manufactures, before any certificate identity.
manufactures=[]
def mc(n,b):
 manufactures.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
f=(h-24)*x*x+x+1;g=(h-24)*x*x+2*x+3
for eta in [23,24,25,27]:
 mat=matrix([fmpz(eta-24),fmpz(1),fmpz(1)],[fmpz(eta-24),fmpz(2),fmpz(3)])
 val=det(mat)[0];mc('formal degree-drop eta'+str(eta),val==(eta-24)*(4*(eta-24)-1));mc('Gaussian degree-drop eta'+str(eta),gauss(mat)==val)
mc('trimmed linear differs',det(matrix([fmpz(1),fmpz(1)],[fmpz(2),fmpz(3)]))[0]==1)
mat=[[fmpz(0),fmpz(2)],[fmpz(3),fmpz(4)]];mc('row-swap determinant',det(mat)[0]==-6 and gauss(mat)==-6)
(V/'OUTER_MANUFACTURES.json').write_text(json.dumps(dict(utc=utc(),status='PASS',count=len(manufactures),checks=manufactures,driver_sha256=sha(__file__),proof_sha256=sha(R/'OUTER_CHECKPOINT_PROOF.md')),indent=2)+'\n')
parts=json.loads((V/'PARTITIONS.json').read_text());ids=[p['id']for p in parts if not p['excluded_by_lemma']]
selected=set(sys.argv[1:])if len(sys.argv)>1 else set(ids)
allrows=[]
for cid in ids:
 cf=V/'cases'/(cid+'.json.gz')
 if not cf.exists():continue
 rec=json.loads(gzip.decompress(cf.read_bytes()))
 if rec['status']!='PASS' or not all(z['passed']for z in rec['checks']):continue
 if not all(sha(p)==digest for p,digest in rec['bindings'].items()):continue
 for j,job in enumerate(rec['jobs']):
  out=O/(cid+'__'+str(j)+'.json.gz')
  binds={str(cf):sha(cf),str(Path(__file__)):sha(__file__),str(R/'OUTER_CHECKPOINT_PROOF.md'):sha(R/'OUTER_CHECKPOINT_PROOF.md'),str(V/'OUTER_MANUFACTURES.json'):sha(V/'OUTER_MANUFACTURES.json'),'independent_code/exact_degree21.py':sha('independent_code/exact_degree21.py')}
  # Manufacture timestamps change per invocation, so bind the stable checks and
  # code/proof content rather than the volatile manufacture output timestamp.
  del binds[str(V/'OUTER_MANUFACTURES.json')]
  old=json.loads(gzip.decompress(out.read_bytes()))if out.exists()else None
  if old and old.get('status')=='PASS'and old.get('bindings')==binds and all(z['passed']for z in old['checks'])and [p['eta']for p in old['points']]==list(range(25,25+old['bound']+1)):
   allrows.append(dict(path=str(out),sha256=sha(out),name=job['name'],status='PASS',count=old['count'],samples=len(old['points'])));print('REUSE',job['name'],utc(),flush=True);continue
  if cid not in selected:continue
  if out.exists():out.rename(out.with_name(out.name+'.before_'+utc().replace(':','-')))
  checks=[];points=[];constant=None;started=utc();info={}
  def ck(n,b,e=None):
   checks.append(dict(name=n,passed=bool(b),evidence=e))
   if not b:raise AssertionError((n,e))
  def save(status):
   packwrite(out,dict(status=status,started_utc=started,updated_utc=utc(),name=job['name'],count=len(checks),checks=checks,points=points,constant=str(constant)if constant is not None else None,bindings=binds,**info))
  try:
   f,g=decode(job['f']),decode(job['g']);i=job['var'];m,n=degree(f,i),degree(g,i);a,b=degree(f,2),degree(g,2);B=n*a+m*b;target=decode(job['resultant']);co=univ(target)
   info=dict(bound=B,degrees=[m,n,a,b],target_degree=len(co)-1)
   ck('recomputed degrees',job['degrees']==[m,n,a,b]and m>0 and n>0)
   ck('recomputed bound',job['bound']==B);ck('target degree at most bound',len(co)-1<=B and co[-1]!=0)
   ck('only one remaining node variable',degree(f,1-i)<=0 and degree(g,1-i)<=0)
   aa,bb=coeffs(f,i,m),coeffs(g,i,n)
   print('START',job['name'],'B',B,'matrix',m+n,utc(),flush=True);save('RUNNING')
   for eta in range(25,25+B+1):
    mat=matrix([horner(t,eta)for t in aa],[horner(t,eta)for t in bb]);value,divisions,swaps=det(mat);q=horner(co,eta)
    if constant is None and q and value:constant=fmpq(value,q);info['normalization_point']=eta
    if constant is None:ck('both zero before normalization eta'+str(eta),not q and not value)
    else:ck('exact determinant eta'+str(eta),fmpq(value)==constant*q)
    if eta in [25,26,27]:ck('independent Gaussian eta'+str(eta),gauss(mat)==value)
    points.append(dict(eta=eta,divisions=divisions,swaps=swaps,determinant_sha256=hashlib.sha256(str(value).encode()).hexdigest()))
    if (eta-25)%25==0:save('RUNNING');print('POINT',job['name'],eta,'of',25+B,utc(),flush=True)
   ck('nonzero fixed normalization',constant is not None and constant!=0)
   ck('Bplus1 consecutive exact samples',[p['eta']for p in points]==list(range(25,25+B+1)))
   for path,digest in binds.items():ck('unchanged '+path,sha(path)==digest)
   save('PASS');print('PASS',job['name'],len(checks),utc(),flush=True)
   allrows.append(dict(path=str(out),sha256=sha(out),name=job['name'],status='PASS',count=len(checks),samples=len(points)))
  except BaseException:
   save('FAIL');(O/(cid+'__'+str(j)+'.traceback.txt')).write_text(traceback.format_exc());raise
# A final closure checker must bind all49 reconstruction cases and every job.
(V/'OUTER_INDEX.json').write_text(json.dumps(dict(utc=utc(),status='PARTIAL_REQUIRES_FINAL_COVERAGE_GATE',jobs=allrows,count=sum(z['count']for z in allrows),samples=sum(z['samples']for z in allrows),driver_sha256=sha(__file__),manufactures_sha256=sha(V/'OUTER_MANUFACTURES.json')),indent=2)+'\n')
