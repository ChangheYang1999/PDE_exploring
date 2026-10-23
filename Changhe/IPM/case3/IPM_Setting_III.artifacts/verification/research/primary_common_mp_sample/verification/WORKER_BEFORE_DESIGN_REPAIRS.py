from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,os,sys,platform
if sys.flags.optimize:raise RuntimeError('optimized refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
import mpmath as mp
import smooth_mp_primitives as impl
R=ROOT/'research/primary_common_mp_sample';V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
def write(p,d):
 t=Path(str(p)+'.tmp');t.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n');os.replace(t,p)
def manufacture():
 checks=[]
 def ck(n,b):
  checks.append(dict(name=n,passed=bool(b)))
  if not b:raise AssertionError(n)
 for alpha,a,L in [(F(1,3),F(1),F(1)),(F(2,5),F(-3,2),F(7,3)),(F(1,5),F(4),F(2))]:
  def q(v):return dict(numerator=str(v.numerator),denominator=str(v.denominator))
  inp=dict(alpha=q(alpha),length=q(L),cl=q(F(5,2)),chebyshev_coefficients=[[q(a)]])
  m=impl.SmoothMP(inp,75);ck('one-mode exact contact strain '+str((alpha,a,L)),m.c==-a/4 and m.a0==a)
  with mp.workdps(100):
   x,y=mp.mpf('.375'),mp.mpf('1.25');aa=impl.number(alpha);av=impl.number(a);ll=impl.number(L);den=1+(x*x+y*y)/(ll*ll);vals=m.fields(x,y)
   expected=[av*y*den**(-aa),-2*aa*av*x*y/ll**2*den**(-aa-1),av*den**(-aa)-2*aa*av*y*y/ll**2*den**(-aa-1)]
   for k,z in zip(['rho','rho_x','rho_y'],expected):ck('one-mode local '+str((alpha,a,L,k)),abs(mp.mpf(vals[k])-z)<=mp.mpf('1e-70')*max(1,abs(z)))
 ck('exact boundary',F(60)**2+F(80)**2==100**2)
 ck('same binary64 key',float('.1').hex()==float(1/10).hex())
 out=dict(status='PASS_PRIMARY_COMMON_SAMPLE_MANUFACTURES',utc=now(),count=len(checks),checks=checks,worker_sha256=sha(__file__),implementation_sha256=sha(impl.__file__),mpmath_version=mp.__version__)
 write(V/'MANUFACTURES.json',out);print(json.dumps({k:out[k]for k in ['status','utc','count']}))
if sys.argv[1:]==['--manufacture']:manufacture();raise SystemExit
if sys.argv[1:]!=['--candidate']:raise SystemExit('use --manufacture or --candidate')
if (V/'candidate').exists():raise FileExistsError('candidate exists')
inputs=json.loads((V/'INPUTS.json').read_text());checks=[];bindings={str(V/'INPUTS.json'):sha(V/'INPUTS.json')}
for p,h in inputs['bindings'].items():
 if sha(p)!=h:raise RuntimeError('input hash '+p)
 bindings[p]=h
man=json.loads((V/'MANUFACTURES.json').read_text())
if not(man['status']=='PASS_PRIMARY_COMMON_SAMPLE_MANUFACTURES'and all(c['passed']for c in man['checks'])and man['worker_sha256']==sha(__file__)and man['implementation_sha256']==sha(impl.__file__)):raise RuntimeError('manufacture gate')
for p in [Path(__file__).resolve(),R/'PROOF.md',V/'MANUFACTURES.json',Path(impl.__file__).resolve()]:bindings[str(p)]=sha(p)
accept=json.loads((V/'DESIGN_ACCEPTANCE.json').read_text())
if accept['status']!='ACCEPTED_FINITE_COMMON_SAMPLE_DESIGN':raise RuntimeError('design not accepted')
for p,h in accept['bindings'].items():
 if sha(p)!=h:raise RuntimeError('design binding '+p)
 bindings[p]=h
bindings[str(V/'DESIGN_ACCEPTANCE.json')]=sha(V/'DESIGN_ACCEPTANCE.json')
# The current wrapper must only launch after333 is finished.
exit333=json.loads((ROOT/'research/angular_integrand_precision/verification/JOB_EXIT.json').read_text())
if exit333['returncode']!=0:raise RuntimeError('333 has not completed successfully')
C=V/'candidate';C.mkdir()
info=dict(status='RUNNING',started_utc=now(),pid=os.getpid(),ppid=os.getppid(),nice=os.getpriority(os.PRIO_PROCESS,0),python=sys.version,executable=sys.executable,module_origins={'smooth_mp_primitives':str(Path(impl.__file__).resolve()),'mpmath':str(Path(mp.__file__).resolve())},mpmath_version=mp.__version__,environment={k:os.environ[k]for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']},bindings=bindings,rows=[])
for row in inputs['states']:
 data=json.loads(Path(row['exact_input']).read_text())
 for digits in [75,110]:
  m=impl.SmoothMP(data,digits);rec=dict(N=row['N'],digits=digits,working_digits=m.working_digits,source_sha256=row['source_sha256'],a_exact=str(m.a0),c_exact=str(m.c),delta_exact=str(m.delta),p_exact=str(m.p),points=[])
  for i,p in enumerate(inputs['points']):
   x,y=map(float.fromhex,p['hex']);rec['points'].append(m.fields(x,y))
   if i%10==0:print(json.dumps(dict(utc=now(),N=row['N'],digits=digits,point=i,total=len(inputs['points']))),flush=True)
   write(C/f"N{row['N']}_d{digits}.json",rec)
  info['rows'].append(dict(N=row['N'],digits=digits,path=str(C/f"N{row['N']}_d{digits}.json"),sha256=sha(C/f"N{row['N']}_d{digits}.json")));write(C/'PROGRESS.json',info)
for p,h in bindings.items():
 if sha(p)!=h:raise RuntimeError('changed during run '+p)
info.update(status='COMPLETE_PRIMARY_COMMON_MP_SAMPLE',finished_utc=now());write(C/'COMPLETE.json',info);print(json.dumps(dict(status=info['status'],finished_utc=info['finished_utc'])),flush=True)
