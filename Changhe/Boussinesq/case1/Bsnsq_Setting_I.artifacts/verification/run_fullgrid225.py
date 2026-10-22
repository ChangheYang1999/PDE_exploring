"""Selected positive-point residual intervals, with visible failures and aborts."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import os,sys,json,hashlib,time,resource,traceback
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
if os.getpriority(os.PRIO_PROCESS,0)!=19 or sys.flags.optimize:raise RuntimeError('nice19 unoptimized required')
r=Path('research/fullgrid_interval225');pp=r/'verification/plan.json';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat()
if len(sys.argv)!=2 or len(sys.argv[1])!=64 or sha(pp)!=sys.argv[1]:raise RuntimeError('external planSHA')
plan=json.loads(pp.read_text())
class IntegrityMismatch(RuntimeError):pass
def pins():
 for p,h in plan['hashes'].items():
  if sha(p)!=h:raise IntegrityMismatch(('integrity mismatch',p))
pins()
if any(k in sys.modules for k in ['dyadic_root220','root220_replay_arithmetic','interval_residual221']):raise RuntimeError('fresh process required')
from dyadic_root220 import Field as Root,I,B
import root220_replay_arithmetic as Other
from interval_residual221 import Field
if B!=(1<<400)or Other.UNIT!=(1<<512)or plan['trial_bits']!=[160,140,120]:raise RuntimeError('arithmetic plan')
(r/'certificates').mkdir(exist_ok=True);dest=r/'certificates/producer.jsonl'
if dest.exists():raise RuntimeError('output exists')
start=time.monotonic();summary={'start_utc':now(),'status':'RUNNING','pid':os.getpid(),'nice':19,'plan_sha256':sha(pp),'total':0,'certified':0,'failed':0}
def save():
 u=resource.getrusage(resource.RUSAGE_SELF);summary.update(updated_utc=now(),elapsed_seconds=time.monotonic()-start,cpu_seconds=u.ru_utime+u.ru_stime);(r/'verification/producer_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
save()
try:
 with dest.open('x')as out:
  for src in plan['sources']:
   if sha(src['input'])!=src['input_sha256']or sha(src['source'])!=src['source_sha256']:raise IntegrityMismatch('direct input/source binding')
   j=json.loads(Path(src['input']).read_text())
   if j['source_sha256']!=src['source_sha256']:raise IntegrityMismatch('JSON source binding')
   root=Root(j);other=Other.Function(j);field=Field(j)
   for item in src['selected']:
    pins();x,y=map(F,item['coordinate_exact_dyadics']);hint=F(item['eta_hint'])
    if x<=0 or y<=0:raise IntegrityMismatch('positive selected grid only')
    rec={'utc':now(),'name':src['name'],'index':item['index'],'source_sha256':src['source_sha256'],'input_sha256':src['input_sha256'],'x':str(x),'y':str(y),'trials':[],'plan_sha256':sha(pp)}
    try:
     bracket=None
     for bits in plan['trial_bits']:
      unit=1<<bits;n=hint.numerator*unit//hint.denominator;l,h=F(n-1,unit),F(n+2,unit);trial={'bits':bits,'l':str(l),'h':str(h)}
      try:
       a,b=root.gx(x,l),root.gx(x,h);c,d=other.gx(x,l),other.gx(x,h)
       strict=a.hi*y.denominator<y.numerator*B<b.lo*y.denominator and c[1]*y.denominator<y.numerator*Other.UNIT<d[0]*y.denominator
       trial.update(gx400_l=a.dump(),gx400_h=b.dump(),gx512_l=list(map(str,c)),gx512_h=list(map(str,d)),status='STRICT'if strict else'INSUFFICIENT_SEPARATION');rec['trials'].append(trial)
       if strict:bracket=(l,h);break
      except MemoryError:raise
      except Exception as e:trial.update(status='FAILED',exception=repr(e));rec['trials'].append(trial)
     if bracket is None:raise ArithmeticError('no strict root enclosure')
     l,h=bracket;eta=I(I.of(l).lo,I.of(h).hi);vals=field.residual(x,eta)
     rec.update(selected_trial=len(rec['trials'])-1,fields={k:v.dump()if v is not None else None for k,v in vals.items()})
     if not vals['y'].contains(y)or vals['A'].lo<=0:raise ArithmeticError('physical root or Jacobian enclosure')
     if vals['N'].lo<=0 or vals['N2'].lo<=0 or vals['prompt_ratio']is None or vals['grouped_ratio']is None:raise ArithmeticError('normalizer enclosure')
     if vals['D']is None:raise ArithmeticError('divided denominator enclosure contains zero')
     rec['status']='CERTIFIED'
    except MemoryError:raise
    except Exception as e:rec.update(status='FAILED',exception=repr(e),traceback=traceback.format_exc())
    out.write(json.dumps(rec,separators=(',',':'))+'\n');out.flush();summary['total']+=1;summary['certified'if rec['status']=='CERTIFIED'else'failed']+=1;save();print(now(),rec['name'],rec['index'],rec['status'],'elapsed',summary['elapsed_seconds'],flush=True)
 pins();summary.update(status='COMPLETE_FINITE_INTERVAL_ATTEMPTS',end_utc=now(),output_sha256=sha(dest));save();print(now(),summary['status'],summary['total'],summary['certified'],summary['failed'],flush=True)
except Exception as e:
 summary.update(status='ABORTED_RESOURCE'if isinstance(e,MemoryError)else'ABORTED_INTEGRITY_MISMATCH'if isinstance(e,IntegrityMismatch)else'ABORTED_UNEXPECTED',exception=repr(e),traceback=traceback.format_exc());save();raise
