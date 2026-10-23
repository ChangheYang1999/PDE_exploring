"""Recompute all degree23 formal resultants with exact native determinants."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,gzip,resource,traceback,sys
import flint
from flint import fmpq
from exact_degree21 import decode,degree,univ
from degree23_native_determinant import coeffs,matrix,horner,det,gauss,native,dispatch_metadata
R=Path('research/degree23_grouped_moment_obstruction');V=R/'verification';O=V/'outer_native'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
utc=lambda:datetime.now(timezone.utc).isoformat()
def packwrite(path,data):
 tmp=path.with_suffix('.tmp');tmp.write_bytes(gzip.compress((json.dumps(data,indent=1)+'\n').encode(),compresslevel=6,mtime=0));tmp.replace(path)
def main():
 resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3))
 if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(1000000)
 assert Path.cwd().resolve()==Path('verification')
 assert Path(__file__).resolve()==Path('independent_code/check_degree23_outer_native.py').resolve()
 assert sys.argv[1:]in ([],['--smoke'])
 smoke=sys.argv[1:]==['--smoke']
 O.mkdir(exist_ok=True)
 assert flint.__version__=='0.9.0' and flint.__FLINT_VERSION__=='3.6.0' and flint.ctx.threads==1
 paths=[Path('independent_code/check_degree23_outer_native.py'),Path('independent_code/degree23_native_determinant.py'),Path('independent_code/exact_degree21.py'),R/'NATIVE_DETERMINANT_PROOF.md',R/'NATIVE_REVIEW_RESOLUTION_PROOF.md',R/'NATIVE_CLOSURE_PROOF.md',R/'OUTER_CHECKPOINT_PROOF.md',V/'native/MANUFACTURES.json',V/'native/PRIMARY_SOURCES.json']
 manufactures=json.loads((V/'native/MANUFACTURES.json').read_text());assert manufactures['status']=='PASS_MANUFACTURES_AND_TIMINGS_ONLY' and manufactures['count']==len(manufactures['checks'])==138 and all(z['passed']for z in manufactures['checks'])
 assert all(sha(p)==d for p,d in manufactures['bindings'].items())
 source=json.loads((V/'native/PRIMARY_SOURCES.json').read_text())
 for row in source:
  if 'sha256'in row:
   p=V/'native'/row['name'];assert sha(p)==row['sha256'];paths.append(p)
 common={str(p):sha(p)for p in paths};parts=json.loads((V/'PARTITIONS.json').read_text());ids=[p['id']for p in parts if not p['excluded_by_lemma']];assert len(ids)==49
 todo=[]
 for cid in ids:
  cf=V/'cases'/(cid+'.json.gz');rec=json.loads(gzip.decompress(cf.read_bytes()))
  assert rec['status']=='PASS'and rec['count']==len(rec['checks'])and all(z['passed']for z in rec['checks'])and all(sha(p)==d for p,d in rec['bindings'].items())
  for j,job in enumerate(rec['jobs']):todo.append((cid,cf,j,job))
 assert len(todo)==82
 if smoke:todo=todo[:1]
 allrows=[]
 for cid,cf,j,job in todo:
  out=O/(cid+'__'+str(j)+'.json.gz');binds={**common,str(cf):sha(cf)}
  old=json.loads(gzip.decompress(out.read_bytes()))if out.exists()else None
  if old and old.get('status')=='PASS'and old.get('bindings')==binds and old.get('algorithm')=='flint_fmpz_mat_det_proved'and old['count']==len(old['checks'])and all(z['passed']for z in old['checks'])and [p['eta']for p in old['points']]==list(range(25,25+old['bound']+1)):
   allrows.append(dict(path=str(out),sha256=sha(out),name=job['name'],status='PASS',count=old['count'],samples=len(old['points'])));print('REUSE',job['name'],utc(),flush=True);continue
  if out.exists():out.rename(out.with_name(out.name+'.before_'+utc().replace(':','-')))
  checks=[];points=[];constant=None;started=utc();info={}
  def ck(n,b,e=None):
   checks.append(dict(name=n,passed=bool(b),evidence=e))
   if not b:raise AssertionError((n,e))
  def save(status):packwrite(out,dict(status=status,algorithm='flint_fmpz_mat_det_proved',python_flint=flint.__version__,flint=flint.__FLINT_VERSION__,flint_threads=flint.ctx.threads,started_utc=started,updated_utc=utc(),name=job['name'],count=len(checks),checks=checks,points=points,constant=str(constant)if constant is not None else None,bindings=binds,**info))
  try:
   f,g=decode(job['f']),decode(job['g']);i=job['var'];m,n=degree(f,i),degree(g,i);a,b=degree(f,2),degree(g,2);B=n*a+m*b;target=decode(job['resultant']);co=univ(target)
   info=dict(bound=B,degrees=[m,n,a,b],target_degree=len(co)-1)
   ck('variable schema',i in [0,1]and len(f.degrees())==len(g.degrees())==3)
   ck('recomputed degrees',job['degrees']==[m,n,a,b]and m>0 and n>0)
   ck('recomputed bound',job['bound']==B);ck('target degree at most bound',len(co)-1<=B and co[-1]!=0)
   ck('only one remaining node variable',degree(f,1-i)<=0 and degree(g,1-i)<=0)
   aa,bb=coeffs(f,i,m),coeffs(g,i,n)
   print('START',job['name'],'B',B,'matrix',m+n,utc(),flush=True);save('RUNNING')
   diagnostic={25,26,27,25+B//2,25+B}
   for eta in range(25,25+B+1):
    mat=matrix([horner(t,eta)for t in aa],[horner(t,eta)for t in bb]);value=native(mat);q=horner(co,eta)
    if constant is None and q and value:constant=fmpq(value,q);info['normalization_point']=eta
    if constant is None:ck('both zero before normalization eta'+str(eta),not q and not value)
    else:ck('exact determinant eta'+str(eta),fmpq(value)==constant*q)
    diagnostic_data={}
    if eta in diagnostic or value==0:
     bv,divisions,swaps=det(mat);ck('independent Bareiss eta'+str(eta),bv==value);diagnostic_data=dict(bareiss_divisions=divisions,bareiss_swaps=swaps)
    if eta in [25,26,27]:ck('independent Gaussian eta'+str(eta),gauss(mat)==value)
    points.append(dict(eta=eta,algorithm='flint_fmpz_mat_det_proved',determinant_sha256=hashlib.sha256(str(value).encode()).hexdigest(),native_value_is_zero=bool(value==0),dispatch=dispatch_metadata(mat),**diagnostic_data))
    if (eta-25)%25==0:save('RUNNING');print('POINT',job['name'],eta,'of',25+B,utc(),flush=True)
   ck('nonzero fixed normalization',constant is not None and constant!=0)
   ck('Bplus1 consecutive exact samples',[p['eta']for p in points]==list(range(25,25+B+1)))
   for path,digest in binds.items():ck('unchanged '+path,sha(path)==digest)
   save('PASS');print('PASS',job['name'],len(checks),utc(),flush=True)
   allrows.append(dict(path=str(out),sha256=sha(out),name=job['name'],status='PASS',count=len(checks),samples=len(points)))
  except BaseException:
   save('FAIL');(O/(cid+'__'+str(j)+'.traceback.txt')).write_text(traceback.format_exc());raise
 assert len(allrows)==len(todo) and len({z['name']for z in allrows})==len(todo)
 (V/('OUTER_NATIVE_SMOKE_INDEX.json'if smoke else'OUTER_NATIVE_INDEX.json')).write_text(json.dumps(dict(utc=utc(),status='SMOKE_ONLY'if smoke else'COMPLETE_REQUIRES_FINAL_COVERAGE_GATE',jobs=allrows,count=sum(z['count']for z in allrows),samples=sum(z['samples']for z in allrows),bindings=common),indent=2)+'\n')
if __name__=='__main__':main()
