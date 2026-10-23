"""Bound native determinant manufactures and a small actual-matrix benchmark."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
import json,hashlib,gzip,random,sys,time,platform
from datetime import datetime,timezone
import flint
from degree23_native_determinant import det,gauss,native,matrix,coeffs,horner,dispatch_metadata
from exact_degree21 import decode,degree

def main():
 r=Path('research/degree23_grouped_moment_obstruction');v=r/'verification/native';v.mkdir(exist_ok=True)
 sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
 paths=[Path(__file__),Path('independent_code/degree23_native_determinant.py'),Path('independent_code/exact_degree21.py'),r/'NATIVE_DETERMINANT_PROOF.md',r/'NATIVE_REVIEW_RESOLUTION_PROOF.md',r/'NATIVE_CLOSURE_PROOF.md',Path('independent_code/check_degree23_outer.py')]
 bindings={str(p):sha(p)for p in paths};start=datetime.now(timezone.utc).isoformat();checks=[];rows=[]
 def ck(n,b,e=None):
  checks.append(dict(name=n,passed=bool(b),evidence=e))
  if not b:raise AssertionError((n,e))
 def test(label,a,expected=None,do_gauss=True):
  t=time.monotonic();nv=native(a);nt=time.monotonic()-t;t=time.monotonic();bv=det(a)[0];bt=time.monotonic()-t
  ck(label+' Bareiss',nv==bv)
  if do_gauss:ck(label+' Gaussian',nv==gauss(a))
  if expected is not None:ck(label+' analytic',nv==expected)
  rows.append(dict(name=label,size=len(a),dispatch=dispatch_metadata(a),native_seconds=nt,bareiss_seconds=bt,determinant_sha256=hashlib.sha256(str(nv).encode()).hexdigest()))
 for eta in [23,24,25,27]:test('formal-drop'+str(eta),matrix([flint.fmpz(eta-24),flint.fmpz(1),flint.fmpz(1)],[flint.fmpz(eta-24),flint.fmpz(2),flint.fmpz(3)]),(eta-24)*(4*(eta-24)-1))
 test('trimmed linear',matrix([flint.fmpz(1),flint.fmpz(1)],[flint.fmpz(2),flint.fmpz(3)]),1)
 test('row swap',[[flint.fmpz(0),flint.fmpz(2)],[flint.fmpz(3),flint.fmpz(4)]],-6)
 rng=random.Random(230022)
 for n in [1,2,3,4,5,7,10,12,26]:
  for k in range(2):
   a=[[flint.fmpz(rng.randrange(-10,11))for j in range(n)]for i in range(n)];test('random'+str(n)+'_'+str(k),a)
  a=[[flint.fmpz(i+1 if i==j else rng.randrange(-9,10)if i<j else 0)for j in range(n)]for i in range(n)]
  import math
  test('triangular'+str(n),a,math.factorial(n))
  if n>1:a[-1]=a[0][:];test('singular'+str(n),a,0)
 for n in [77,87]:
  a=[[flint.fmpz(1+(i==j))for j in range(n)]for i in range(n)];test('large dense'+str(n),a,n+1)
  a[-1]=a[0][:];test('large singular'+str(n),a,0)
  a[-1][-1]+=1;test('large near singular'+str(n),a)
 for text in ['7/13','-53/17']:ck('rational string roundtrip '+text,str(flint.fmpq(text))==text)
 for cid,j in [('1_3_2_2_1_1_1_1',0),('1_3_2_2_1_1_1_1',1)]:
  p=v.parent/'cases'/(cid+'.json.gz');bindings[str(p)]=sha(p);job=json.loads(gzip.decompress(p.read_bytes()))['jobs'][j]
  f,g=decode(job['f']),decode(job['g']);i=job['var'];aa=coeffs(f,i,degree(f,i));bb=coeffs(g,i,degree(g,i))
  for eta in [25,1000]:test(job['name']+' eta'+str(eta),matrix([horner(a,eta)for a in aa],[horner(b,eta)for b in bb]),do_gauss=eta==25)
 for p,d in bindings.items():ck('unchanged '+p,sha(p)==d)
 ck('single FLINT thread',flint.ctx.threads==1)
 obj=dict(status='PASS_MANUFACTURES_AND_TIMINGS_ONLY',started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,rows=rows,bindings=bindings,python=sys.version,executable=sys.executable,python_flint=flint.__version__,flint=flint.__FLINT_VERSION__,flint_threads=flint.ctx.threads,scope='Native determinant diagnostics only; no completed degree23 identity or primary endpoint implied.')
 (v/'MANUFACTURES.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:obj[k]for k in ['status','count','started_utc','finished_utc','python_flint','flint']}));print(json.dumps(rows[-4:],indent=2))
if __name__=='__main__':main()
