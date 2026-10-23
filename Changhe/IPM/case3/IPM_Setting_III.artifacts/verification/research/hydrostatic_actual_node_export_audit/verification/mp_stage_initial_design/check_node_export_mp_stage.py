"""Finite-moment, same-shape geometry and real MP restart manufactures."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import os,sys,json,time,hashlib,gzip,signal,subprocess
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
import numpy as np
import mpmath as mp
from node_export_mp_chunks import MPChunkStore,digest_rows,encode_values,decimal_value
from node_export_mp_integrand import frozen_geometry,exact_moments,exact_components,compare_decimal_rows,MOMENT_NAMES,COMPONENT_NAMES
from node_export_inverse_stage import RULES,evaluate
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';D=V/'mp_stage_manufactures';D.mkdir(exist_ok=True)
def rational(i):
 x=mp.mpf(i-20)/8;y=mp.mpf(i%9)/16;a=1+x*x+y*y
 return [-2*x*y/a**2,-2*y/a**2+8*x*x*y/a**3]
if len(sys.argv)>1 and sys.argv[1]=='--child':
 def stop(n):
  if sys.argv[3]=='stop'and n==64:os.kill(os.getpid(),signal.SIGTERM)
 MPChunkStore(Path(sys.argv[2]),75,72,2,{'synthetic':'rational75'}).run(rational,stop);raise SystemExit(0)
now=lambda:datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();start=now();tick=time.perf_counter();checks=[];bindings={}
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=str(p);z=sha(p);ck('binding '+p,h is None or z==h);bindings[p]=z
def rejected(n,fun):
 try:fun()
 except (ValueError,TypeError,ArithmeticError,KeyError)as e:ck(n,True,str(e));return
 ck(n,False)
def jet(x,y):
 x,y=np.broadcast_arrays(x,y);a=1+x*x+y*y
 return np.stack([y/a,-2*x*y/a**2,1/a-2*y*y/a**2,-2*y/a**2+8*x*x*y/a**3],axis=-1)
try:
 for p in [__file__,'independent_code/node_export_mp_chunks.py','independent_code/node_export_mp_integrand.py','independent_code/node_export_inverse_stage.py','independent_code/independent_hydrostatic.py','independent_code/run_actual_node_mp_inverse.py',R/'MP_INTEGRAND_EXECUTION_PROOF.md']:bind(p)
 for label in RULES:
  for x,y in [(0.,0.),(0.,.5),(.75,0.),(.75,.5),(-.75,-.5)]:
   g=frozen_geometry(jet,x,y,.5,RULES[label]);z=evaluate(jet,x,y,.5,RULES[label]);ref=np.r_[z['V'],z['Phi'],z['dV2_dy'],z['tail_V']]
   ck('bitwise same vector-shape rule '+str((label,x,y)),g['reference'].tobytes()==ref.tobytes()and g['metadata'].tobytes()==z['meta'].tobytes())
   mm=exact_moments(g);cc=exact_components(mm,x,y)
   for k,v in cc.items():ck('finite exact moment '+str((label,x,y,k)),abs(float(v)-ref[COMPONENT_NAMES.index(k)])<3e-12)
 # Independently assembled rational moment sums at arbitrary dyadic geometry, including both axes.
 for x,y in [(0.,0.),(.75,0.),(0.,.5),(.75,.5),(-.75,-.5)]:
  n=np.array([0.,.125,.25,.5,1.,2.]);w=np.array([.125,.25,.25,.5,1.,2.]);ph=np.array([0,0,1,1,2,2],np.int8);j=jet(abs(x),n)[:,[1,3]];g=dict(node=n,weight=w,phase=ph,derivatives=j)
  rows=[];wanted=[F(0)]*6
  for i,t in enumerate(n):
   xx,tt,ww=map(F,map(float,[abs(x),t,w[i]]));a=1+xx*xx+tt*tt;gx=-2*xx*tt/a**2;gxx=-2*tt/a**2+8*xx*xx*tt/a**3
   with mp.workdps(108):row=encode_values([mp.mpf(gx.numerator)/gx.denominator,mp.mpf(gxx.numerator)/gxx.denominator],108,2)
   rows.append(row)
   for k,val in enumerate([gx,gxx]):wanted[2*ph[i]+k]+=ww*(tt if ph[i]==0 else 1)*val
  m=exact_moments(g,rows);c=exact_components(m,x,y)
  for k,want in zip(MOMENT_NAMES,wanted):ck('rational moment oracle '+str((x,y,k)),abs(m[k]-want)<=max(abs(want),F(1,10**80))*F(1,10**100))
  double=exact_components(exact_moments(g),x,y);b={k:F(float(v))for k,v in double.items()}
  for k in COMPONENT_NAMES:ck('sensitivity identity '+str((x,y,k)),c[k]-b[k]==(c[k]-double[k])+(double[k]-b[k]))
 for name in ['full','resumed']:
  if (D/name).exists():raise FileExistsError('preserve old manufacture '+name)
 full=MPChunkStore(D/'full',75,72,2,{'synthetic':'rational75'}).run(rational)
 p=subprocess.run([sys.executable,__file__,'--child',str(D/'resumed'),'stop'],timeout=30,capture_output=True,text=True);ck('actual MP SIGTERM after64',p.returncode==-signal.SIGTERM,dict(returncode=p.returncode,stderr=p.stderr))
 ck('one complete chunk retained',sorted(p.name for p in (D/'resumed').glob('chunk_*.json.gz'))==['chunk_0000000.json.gz'])
 p=subprocess.run([sys.executable,__file__,'--child',str(D/'resumed'),'resume'],timeout=30,capture_output=True,text=True);ck('fresh process MP resume',p.returncode==0,dict(returncode=p.returncode,stderr=p.stderr))
 for path in (D/'full').glob('chunk_*.json.gz'):ck('identical resumed compressed bytes '+path.name,path.read_bytes()==(D/'resumed'/path.name).read_bytes())
 hashes={str(p):sha(p)for p in (D/'resumed').glob('chunk_*.json.gz')};got=MPChunkStore(D/'resumed',75,72,2,{'synthetic':'rational75'}).run(rational);ck('all75same decimals',got==full);ck('completed MP resume no writes',all(sha(p)==h for p,h in hashes.items()))
 for kw in [dict(digits=108),dict(width=4),dict(total=74),dict(bindings={'synthetic':'changed'})]:
  base=dict(directory=D/'resumed',total=75,digits=72,width=2,bindings={'synthetic':'rational75'});base.update(kw);rejected('signature mismatch '+str(kw),lambda base=base:MPChunkStore(**base).run(rational))
 original=json.loads(gzip.decompress((D/'full/chunk_0000000.json.gz').read_bytes()))
 for kind in ['interval','short','shape','nonfinite','digest','finite_replay']:
  d=json.loads(json.dumps(original));dest=D/('tamper_'+kind);dest.mkdir()
  if kind=='interval':d['start']=1
  elif kind=='short':d['rows'].pop()
  elif kind=='shape':d['rows'][0].append('0.0')
  elif kind=='nonfinite':d['rows'][0][0]='nan'
  elif kind=='digest':d['rows'][2][0]='17.0'
  elif kind=='finite_replay':d['rows'][-1][0]='17.0';d['rows_sha256']=digest_rows(d['rows'])
  (dest/'chunk_0000000.json.gz').write_bytes(gzip.compress(json.dumps(d).encode(),mtime=0));rejected('MP tampered '+kind,lambda dest=dest:MPChunkStore(dest,75,72,2,{'synthetic':'rational75'}).run(rational))
 lo=[['0.0','1e-90'],['1.0','2.0']];hi=[['0.0','2e-90'],['1.0000000000000000000000000000000000000000000000000001','2.0']];dd=np.array([[0.,0.],[1.,2.]])
 comp=compare_decimal_rows(lo,hi,dd,'1e-80','1e-48');ck('precision failures preserved',not comp['precision_diagnostic_passed']and len(comp['precision_failed_entries'])==1);ck('zero and nearzero counts',comp['zero_counts']==[1,0]and comp['nearzero_counts']==[1,1])
 for bad in ['nan','inf','1/3','0x12',1.,'', '1e99999999']:
  rejected('bad decimal '+str(bad),lambda bad=bad:decimal_value(bad))
 for p,h in list(bindings.items()):ck('stable '+p,sha(p)==h)
 status='PASS_MP_GEOMETRY_MOMENTS_AND_REAL_RESTART'
except Exception:
 import traceback
 status='FAIL';error=traceback.format_exc();raise
finally:
 out=dict(status=status,started_utc=start,finished_utc=now(),elapsed_seconds=time.perf_counter()-tick,count=len(checks),checks=checks,bindings=bindings,error=locals().get('error'),artifacts={str(p):sha(p)for p in D.glob('*/*.json.gz')},scope='Synthetic finite checks, no candidate MP inverse or error bound.')
 (V/'MP_STAGE_MANUFACTURES.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(status,len(checks),out['elapsed_seconds'])
