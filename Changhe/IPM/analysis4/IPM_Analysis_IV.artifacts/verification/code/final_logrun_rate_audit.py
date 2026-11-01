"""Independent finite norm/rate audit with explicit canonical-prefix cutoffs."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from decimal import Decimal
from hashlib import sha256
import json,pickle,time,sys,gc
sys.dont_write_bytecode=True
from flint import arb,fmpz,ctx
from read_evidence_bytes import read_bytes
base=Path('research/306_final_logrun_rates');start=time.monotonic()
def ref(p,raw=None):
 if raw is None:raw=p.read_bytes()
 return dict(path=str(p),sha256=sha256(raw).hexdigest())
def unpack(v):
 if len(v)==3:
  m,e,rs=v
  r,re=(0,0) if rs=='0' else rs.split('*2^')
 else:m,e,r,re=v
 mid=arb(fmpz(int(m)))*arb(2)**int(e);rad=arb(fmpz(int(r)))*arb(2)**int(re)
 assert mid.is_exact() and rad.is_exact() and rad>=0
 return arb(mid,rad)
def exact(x):
 x=F(x);return arb(x.numerator)/x.denominator
def values(logs,N):
 steps={n:logs[n]-logs[n-1] for n in range(N-29,N+1)}
 mean=(logs[N]-logs[N-30])/30
 assert mean.overlaps(sum(steps.values(),arb(0))/30)
 lower=min(float(x.lower()) for x in steps.values());upper=max(float(x.upper()) for x in steps.values())
 root=(logs[N]*arb(10).log()/N).exp()
 return dict(mean=mean,root=root,minimum_enclosure=arb(min(x.lower() for x in steps.values()),0),maximum_enclosure=arb(max(x.upper() for x in steps.values()),0)),steps
cases=[('4/9',300,'log_sin1_c9_5_p512','-0.328','0.4576'),('2/5',240,'log_sin1_c5_3_p512','-0.254','0.5387'),('9/20',240,'log_sin1_c20_11_p512','-0.338','0.4450'),('1/2',300,None,'-0.419','0.3716'),('2/3',329,None,'-0.691','0.1952')]
results=[]
for delta,N,tag,printed_mean,printed_root in cases:
 timer=time.monotonic();input_kind=None;coefficient_count=None
 if tag:
  p=Path('../a4-num/ckpt')/(tag+'.pkl');before=p.stat();raw=p.read_bytes();metadata=ref(p,raw);s=pickle.loads(raw);del raw
  assert (before.st_size,before.st_mtime_ns)==(p.stat().st_size,p.stat().st_mtime_ns)
  assert s['ring']=='arb' and s['prec']==512 and F(int(s['A']),int(s['B']))==F(delta) and max(s['f'])==N
  states=[s['f'][n] for n in range(N-30,N+1)]
  coefficient_count=sum(len(col) for cols in states for col in cols)
  input_kind='independent absolute-value norm sums of supplied checkpoint coefficient balls'
  input_logs=[];scalar_norms=[]
  for bits in (768,1536):
   ctx.prec=bits;logs={};norms={}
   for n,cols in zip(range(N-30,N+1),states):
    norm=sum((abs(unpack(v)) for col in cols for v in col),arb(0));assert norm>0
    norms[n]=norm;logs[n]=norm.log()/arb(10).log()
   input_logs.append(logs);scalar_norms.append(norms)
  del s,states;gc.collect()
 elif delta=='1/2':
  p=Path('research/291_canonical_half_finite/verification/checks.json');raw=read_bytes(p);metadata=ref(p,raw);s=json.loads(raw);assert s['all_checks_pass']
  normdata={r['n']:r['fields']['f']['norm'] for r in s['rows'] if N-30<=r['n']<=N}
  input_logs=[];scalar_norms=[]
  for bits in (768,1536):
   ctx.prec=bits;norms={n:unpack(v) for n,v in normdata.items()};assert all(x>0 for x in norms.values())
   scalar_norms.append(norms);input_logs.append({n:x.log()/arb(10).log() for n,x in norms.items()})
  input_kind='previously independently audited norm balls from topic291'
 else:
  p=Path('research/64_log_precision_updates/verification/log_sin1_c3_p512_N329_20261031T093348Z/checks.json');raw=read_bytes(p);metadata=ref(p,raw);s=json.loads(raw);assert s['maximum_order']==329
  input_kind='previously independently audited log-norm balls from topic64 at the explicit329 cutoff'
  logs_data={r['n']:r['log10_plain_norm'] for r in s['fields']['f']['all_order_factorial_comparisons'] if N-30<=r['n']<=N}
  input_logs=[];scalar_norms=[]
  for bits in (768,1536):
   ctx.prec=bits;input_logs.append({n:arb(v) for n,v in logs_data.items()});scalar_norms.append({})
 calculated=[]
 for bits,logs in zip((768,1536),input_logs):
  ctx.prec=bits;assert sorted(logs)==list(range(N-30,N+1));calculated.append(values(logs,N))
 assert all(input_logs[0][n].overlaps(input_logs[1][n]) for n in input_logs[0])
 assert all(calculated[0][0][k].overlaps(calculated[1][0][k]) for k in ('mean','root'))
 vals,steps=calculated[1]
 comparisons=[]
 for key,printed in [('mean',printed_mean),('root',printed_root)]:
  h=exact(F(10)**Decimal(printed).as_tuple().exponent/2);c=exact(printed);x=vals[key]
  ok=bool(c-h<x and x<c+h);assert ok,(delta,key,printed,x)
  comparisons.append(dict(statistic=key,printed=printed,rounding_unit=str(F(10)**Decimal(printed).as_tuple().exponent),enclosed=x.str(40),within_rounding_bin=ok))
 result=dict(delta=delta,N=N,increment_window=[N-29,N],norm_window=[N-30,N],source=metadata,input_kind=input_kind,coefficient_positions_per_replay=coefficient_count,log_norms={str(n):x.str(45) for n,x in input_logs[1].items()},increments={str(n):x.str(40) for n,x in steps.items()},mean_increment=vals['mean'].str(40),root=vals['root'].str(40),all_increments_negative=all(x<0 for x in steps.values()),comparisons=comparisons,all_precision_replays_overlap=True,actual_elapsed_s=time.monotonic()-timer)
 assert result['all_increments_negative'];results.append(result)
 print(json.dumps({k:result[k] for k in ['delta','N','mean_increment','root','coefficient_positions_per_replay','actual_elapsed_s']}),flush=True)
initial=base/'sources/logrun_rates_initial.json';bad=json.loads(initial.read_text())['2/3 (certified part)'];assert bad['N']==348
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
out=dict(at=now,all_checks_pass=True,bits=[768,1536],cases=results,initial_table=ref(initial),initial_two_thirds_cutoff_mismatch=dict(labeled_N=bad['N'],required_N=329,labeled_mean=bad['mean_inc_last30'],correct_mean=results[-1]['mean_increment']),scope='Finite norm/rate audit under supplied input ball hypotheses; no complete nonlinear replay or infinite asymptotic assertion.',actual_elapsed_s=time.monotonic()-start)
(base/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n');(base/'sources/final_logrun_rate_audit.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(dict(at=now,total_seconds=out['actual_elapsed_s'],all_checks_pass=True)),flush=True)
