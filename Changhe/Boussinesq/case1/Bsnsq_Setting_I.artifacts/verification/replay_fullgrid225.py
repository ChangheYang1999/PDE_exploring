"""Fresh independent root check and rational interval reaggregation, no Taylor import."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import os,sys,json,hashlib,time,resource,traceback
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
if os.getpriority(os.PRIO_PROCESS,0)!=19 or sys.flags.optimize:raise RuntimeError('nice19 unoptimized required')
r=Path('research/fullgrid_interval225');pp=r/'verification/plan.json';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat()
if len(sys.argv)!=2 or len(sys.argv[1])!=64 or sha(pp)!=sys.argv[1]:raise RuntimeError('external planSHA')
plan=json.loads(pp.read_text());checks=0
expected_regions=[['focused_origin_region',0,169],['focused_intermediate',169,338],['focused_outer',338,507],['broad',507,1183]]
class IntegrityMismatch(RuntimeError):pass
def ck(test,label):
 global checks
 if not test:raise IntegrityMismatch(label)
 checks+=1
def pins():
 for p,h in plan['hashes'].items():ck(sha(p)==h,'plan pin '+p)
pins();ck(plan['regions']==expected_regions and plan['quantities']==['prompt_ratio','grouped_ratio','R','D']and plan['tie_rule']=='smallest index','selection contract');tables=json.loads(Path('candidate_audits/core32_focused218/verification/tables.json').read_text());ck(tables['status']=='PASS_EXACT_SAVED_DECIMAL_REGIONAL_ORDERING','bound table status');ck(not any(k in sys.modules for k in ['dyadic_root220','interval_residual221','root220_replay_arithmetic']),'fresh process')
import root220_replay_arithmetic as A
ck('dyadic_root220'not in sys.modules and 'interval_residual221'not in sys.modules,'import isolation')
ck(A.BITS==512,'second precision');producer=r/'certificates/producer.jsonl';pj=json.loads((r/'verification/producer_summary.json').read_text());ck(pj['status']=='COMPLETE_FINITE_INTERVAL_ATTEMPTS'and pj['total']==plan['total'],'producer complete');ck(pj['output_sha256']==sha(producer)and pj['plan_sha256']==sha(pp),'producer binding');prodhash=sha(producer);records=[json.loads(line)for line in producer.read_text().splitlines()];ck(len(records)==plan['total'],'recordcount')
# Fresh exact-rational endpoint operations, independent of the producer I class.
def num(x):x=F(x);return(x,x)
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):v=[x*y for x in a for y in b];return(min(v),max(v))
def inv(a):
 if a[0]<=0<=a[1]:raise ArithmeticError('zero interval denominator')
 return(F(1)/a[1],F(1)/a[0])
def div(a,b):return mul(a,inv(b))
def ab(a):return a if a[0]>=0 else neg(a)if a[1]<=0 else(F(0),max(-a[0],a[1]))
def summ(v):
 out=num(0)
 for a in v:out=add(out,a)
 return out
def contains(a,b):return a[0]<=b[0]<=b[1]<=a[1]
def parse(v):
 ck(isinstance(v,dict)and set(v)=={'lo','hi','denominator_power'}and v['denominator_power']==400,'400 interval shape');a,b=int(v['lo']),int(v['hi']);ck(str(a)==v['lo']and str(b)==v['hi']and a<=b,'canonical integer endpoints');return(F(a,1<<400),F(b,1<<400))
def serial(a):return list(map(str,a))
output=r/'certificates/replay.jsonl';ck(not output.exists(),'fresh output');start=time.monotonic();summary={'start_utc':now(),'status':'RUNNING','pid':os.getpid(),'nice':19,'plan_sha256':sha(pp),'producer_sha256':prodhash,'producer_summary_sha256':sha(r/'verification/producer_summary.json'),'total':0,'certified':0,'failed':0,'R_excludes_zero':0,'states':{},'scope':'Complete finite prescribed grid if all succeed; no regional supremum. Fresh512 root check and rational aggregation, no fresh fourth derivatives.'}
def save():
 u=resource.getrusage(resource.RUSAGE_SELF);summary.update(updated_utc=now(),elapsed_seconds=time.monotonic()-start,cpu_seconds=u.ru_utime+u.ru_stime,checks=checks);(r/'verification/replay_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
save();at=0
try:
 with output.open('x')as out:
  for src in plan['sources']:
   ck(sha(src['input'])==src['input_sha256']and sha(src['source'])==src['source_sha256'],'exact source bytes');data=json.loads(Path(src['input']).read_text());ck(data['source_sha256']==src['source_sha256'],'JSONsource');field=A.Function(data)
   raw={}
   for seg in src['raw_segments']:
    ck(sha(seg['path'])==seg['sha256'],'raw segmentpin');raw.update({v['index']:v for v in map(json.loads,Path(seg['path']).read_text().splitlines())})
   ck(sorted(raw)==list(range(1183)),'joint raw completeness');reasons={}
   for i,v in raw.items():
    xx,yy=map(F,v['coordinate_exact_dyadics']);ck(xx>0 and yy>0 and v['status']=='COMPUTED'and v['dps']==130 and v['source_sha256']==src['source_sha256'],'positive finite raw domain')
    for key in plan['quantities']+['eta']:F(v['fields'][key])
   for label,lo,hi in expected_regions:
    tab=[v for v in tables['rows']if v['name']==src['name']and v['region']==label];ck(len(tab)==1 and tab[0]['point_count']==hi-lo and set(tab[0]['maxima'])==set(plan['quantities']),'table region and quantities');tab=tab[0]
    for key in plan['quantities']:
     idx=max(range(lo,hi),key=lambda i:abs(F(raw[i]['fields'][key])));ck(tab['maxima'][key]['index']==idx and F(tab['maxima'][key]['absolute_value'])==abs(F(raw[idx]['fields'][key])),'raw maximum and smallest-index tie');reasons.setdefault(idx,[]).append([label,key])
   reasons={i:[[label,'full_grid']]for label,lo,hi in expected_regions for i in range(lo,hi)}
   ck([v['index']for v in src['selected']]==sorted(reasons),'independent finite selection');state={'certified':0,'failed':0,'max_selected_upper':{},'max_selected_lower':{}};summary['states'][src['name']]=state
   for item in src['selected']:
    rec=records[at];at+=1;idx=item['index'];v=raw[idx];x,y=map(F,item['coordinate_exact_dyadics']);hint=F(item['eta_hint']);ck(x>0 and y>0,'positive selected point');ck(item['reasons']==reasons[idx],'selection reasons');ck(item['coordinate_exact_dyadics']==v['coordinate_exact_dyadics']and F(v['fields']['eta'])==hint,'source coordinate hint');ck(rec['name']==src['name']and rec['index']==idx and rec['source_sha256']==src['source_sha256']and rec['input_sha256']==src['input_sha256']and rec['plan_sha256']==sha(pp),'record binding');ck(F(rec['x'])==x and F(rec['y'])==y,'record location');row={'utc':now(),'name':src['name'],'index':idx,'source_sha256':src['source_sha256'],'x':str(x),'y':str(y)}
    ck(0<=len(rec['trials'])<=3,'all-record trial count')
    for ti,tr in enumerate(rec['trials']):
     tb=plan['trial_bits'][ti];tu=1<<tb;tn=hint.numerator*tu//hint.denominator;ck(tr['bits']==tb and F(tr['l'])==F(tn-1,tu)and F(tr['h'])==F(tn+2,tu),'all-record trial prescription');ck(tr['status']in ['FAILED','INSUFFICIENT_SEPARATION','STRICT']and(tr['status']!='STRICT'or ti==len(rec['trials'])-1),'no trial after strict root')
    ck(any(tr['status']=='STRICT'for tr in rec['trials'])or len(rec['trials'])==len(plan['trial_bits']),'no truncated failed trial sequence')
    if rec['status']=='FAILED':row.update(status='FAILED_PRODUCER',producer_exception=rec['exception']);summary['failed']+=1;state['failed']+=1
    else:
     ck(rec['status']=='CERTIFIED','known producer status');k=rec['selected_trial'];ck(type(k)is int and 0<=k<len(rec['trials'])<=3 and k==len(rec['trials'])-1,'trial index')
     for ti,tr in enumerate(rec['trials']):
      tb=plan['trial_bits'][ti];tu=1<<tb;tn=hint.numerator*tu//hint.denominator;ck(tr['bits']==tb and F(tr['l'])==F(tn-1,tu)and F(tr['h'])==F(tn+2,tu),'every trial prescribed bracket');ck(tr['status']in(['STRICT']if ti==k else['FAILED','INSUFFICIENT_SEPARATION']),'first accepted trial only')
     trial=rec['trials'][k];bits=plan['trial_bits'][k];unit=1<<bits;n=hint.numerator*unit//hint.denominator;l,h=F(n-1,unit),F(n+2,unit);ck(trial['status']=='STRICT'and trial['bits']==bits and F(trial['l'])==l and F(trial['h'])==h and l<hint<h,'new bracket reconstruction')
     ck(max(l,F(item['old_l']))<=min(h,F(item['old_h'])),'new and220 brackets intersect')
     for side in ['l','h']:
      z=parse(trial['gx400_'+side]);a=list(map(int,trial['gx512_'+side]));ck(len(a)==2 and a[0]<=a[1],'stored512shape');b=(F(a[0],A.UNIT),F(a[1],A.UNIT));ck(z[1]<y and b[1]<y if side=='l'else z[0]>y and b[0]>y,'both stored strict checks')
     a,b=field.gx(x,l),field.gx(x,h);ck(a[1]*y.denominator<y.numerator*A.UNIT<b[0]*y.denominator,'fresh512strictroot');f={k:parse(v)if v is not None else None for k,v in rec['fields'].items()};ck(contains(f['eta'],(l,h))and contains(f['x'],num(x))and contains(f['y'],num(y)),'physical input enclosures');ck(f['A'][0]>0,'Jacobian positive');p=[mul(f['W1'],f['Omega_x']),mul(f['W2'],f['Omega_y']),f['Omega'],neg(f['Theta_x'])];g=[mul(f['U1'],f['Omega_x']),mul(f['U2'],f['Omega_y']),add(mul(num(3),add(mul(f['x'],f['Omega_x']),mul(f['y'],f['Omega_y']))),f['Omega']),neg(f['Theta_x'])]
     expected={'R':summ(p),'N':summ(list(map(ab,p))),'N2':summ(list(map(ab,g))),'D':div(f['R'],mul(f['x'],f['y'])),'R_Theta':sub(add(mul(f['W1'],f['Theta_x']),mul(f['W2'],f['Theta_y'])),f['Theta'])}
     ck(f['N'][0]>0 and f['N2'][0]>0,'normalizerspositive');expected['prompt_ratio']=div(ab(f['R']),f['N']);expected['grouped_ratio']=div(ab(f['R']),f['N2'])
     for key,value in expected.items():ck(f[key]is not None and contains(f[key],value),'independent aggregation containment '+key)
     ck(contains(f['R_Theta'],num(0)),'temperature arithmetic consistency only');excludes=expected['R'][0]>0 or expected['R'][1]<0
     row.update(status='CERTIFIED',root_l=str(l),root_h=str(h),fresh_gx512_l=list(map(str,a)),fresh_gx512_h=list(map(str,b)),R_excludes_zero=excludes,reaggregated_R=serial(expected['R']),signed_intervals={key:serial(f[key])for key in ['R','D']},intervals={key:serial(ab(f[key])if key in ['R','D']else f[key])for key in ['R','D','prompt_ratio','grouped_ratio']},scalar_diagnostics={key:{'saved':item['scalar_fields'][key],'inside_producer_interval':contains(f[key],num(F(item['scalar_fields'][key])))}for key in item['scalar_fields']})
     for key in ['R','D','prompt_ratio','grouped_ratio']:
      z=ab(f[key])if key in ['R','D']else f[key]
      for target,pos in [('max_selected_upper',1),('max_selected_lower',0)]:
       if key not in state[target]or z[pos]>F(state[target][key]['bound']):state[target][key]={'index':idx,'bound':str(z[pos])}
     summary['certified']+=1;state['certified']+=1;summary['R_excludes_zero']+=int(excludes)
    out.write(json.dumps(row,separators=(',',':'))+'\n');out.flush();summary['total']+=1;save();print(now(),src['name'],idx,row['status'],flush=True)
 ck(at==plan['total']and sha(producer)==prodhash,'complete stable producer');pins();summary.update(status='COMPLETE_FINITE_INTERVAL_REPLAY'if not summary['failed']else'COMPLETE_WITH_FAILED_INTERVALS',end_utc=now(),output_sha256=sha(output));save();print(now(),summary['status'],summary['total'],summary['certified'],summary['failed'],checks,flush=True)
except Exception as e:
 summary.update(status='ABORTED_RESOURCE'if isinstance(e,MemoryError)else'ABORTED_INTEGRITY_MISMATCH'if isinstance(e,IntegrityMismatch)else'ABORTED_UNEXPECTED',exception=repr(e),traceback=traceback.format_exc());save();raise
