"""Independent supplementary333 audit; no field evaluator imported."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
import json, gzip, hashlib, math, sys
import numpy as np
ROOT=Path('verification')
assert Path.cwd().resolve()==ROOT and not sys.flags.optimize
R=ROOT/'research/angular_integrand_precision'; V=R/'verification'; C=V/'candidate'
checks=[]; bindings={}
def ck(name, condition, evidence=None):
 checks.append(dict(name=name,passed=bool(condition),evidence=evidence))
 if not condition: raise AssertionError(name)
def bind(p, expected=None):
 p=Path(p).resolve(); b=p.read_bytes(); h=hashlib.sha256(b).hexdigest()
 ck('stable '+str(p),p.read_bytes()==b and (expected is None or h==expected))
 bindings[str(p)]=h;return b
def read(p):return json.loads(bind(p))
def rehash(d):
 for p,h in d.items():bind(p,h)
def floats(d):return {k:float(F(v)) if v is not None else None for k,v in d.items()}
for p in [__file__,R/'FINAL_SUPPLEMENT_PROOF.md']:bind(p)
a=read(V/'CHECKS.json');d=read(V/'DISPLAY.json');c=read(C/'COMPLETE.json')
ck('main533',a['count']==533 and len(a['checks'])==533 and all(x['passed']for x in a['checks']) and a['precision_diagnostics_passed'])
ck('display binds exact check',d['input_sha256']==bindings[str((V/'CHECKS.json').resolve())])
rehash(a['bindings']);rehash(c['bindings']);rehash(c['artifacts'])
ck('two display records',len(a['records'])==len(d['records'])==2)
observations=[]
for ar,dr in zip(a['records'],d['records']):
 r=ar['radius'];ck('display identity '+str(r),ar['radius']==dr['radius']and ar['nodes']==dr['nodes'])
 for name in ['local_MP_minus_double','scalar_minus_batch']:ck('display '+name+str(r),dr[name]==[float(F(x))for x in ar[name]])
 for name in ['precision_integrands','precision_local']:ck('display '+name+str(r),ar[name]==dr[name])
 ck('component display '+str(r),dr['component_changes']=={k:floats(v)for k,v in ar['component_ledger'].items()})
 rr=ar['residual_records']; mm0=rr[0]['fields']['MM']; base=F(mm0['Nf']); r0=F(mm0['R']);steps=[];den_changes=[]
 ck('three display steps '+str(r),len(rr)==len(dr['residuals'])==3)
 for row,shown in zip(rr,dr['residuals']):
  step=(F(row['fields']['MM']['R'])-r0)/base; correction=F(row['fixed_Nf_D']['total'])
  ck('epsilon '+str((r,row['epsilon'])),row['epsilon']==shown['epsilon'])
  ck('all displayed fields '+str((r,row['epsilon'])),shown['fields']=={k:floats(v)for k,v in row['fields'].items()})
  ck('display decomposition '+str((r,row['epsilon'])),shown['fixed_Nf_D']==floats(row['fixed_Nf_D']))
  ck('display signed step '+str((r,row['epsilon'])),shown['step_change_fixed_Nf_MM0']==float(step))
  ck('display finite quotient '+str((r,row['epsilon'])),shown['precision_change_to_step_magnitude']==(float(abs(correction/step))if step else None))
  steps.append(step);den_changes.append(float((F(row['fields']['MM']['Nf'])-base)/base))
 observations.append(dict(radius=r,step_ratio_5_to_6=float(steps[1]/steps[2]),step_Nf_relative_changes=den_changes,step_values=list(map(float,steps))))
job=read(V/'JOB.json');design=read(V/'DESIGN_ACCEPTANCE.json');man=read(V/'MANUFACTURES.json');fresh=read(V/'FRESH_ATTEMPT_PREPARATION.json');exit=read(V/'JOB_EXIT.json');prep=read(V/'EXECUTION_PREPARATION.json')
for j in [job,design,man]:rehash(j['bindings'])
ck('actual manufacture57',man['count']==len(man['checks'])==57 and man['status']=='PASS_SELECTED_ANGULAR_MP_MANUFACTURES'and all(x['passed']for x in man['checks']))
ck('accepted fresh design',design['status']=='ACCEPTED_FRESH_BATCH_BASELINE_FINITE_DIAGNOSTIC_ONLY'and design['manufactured_count']==57)
ck('fresh run order',design['utc']<=job['utc']<=c['started_utc']<=c['finished_utc']<=exit['utc']and exit['returncode']==0)
ck('complete127',c['count']==len(c['checks'])==127 and all(x['passed']for x in c['checks']))
for name in ['nice19','memory14GiB','one thread OMP_NUM_THREADS','one thread OPENBLAS_NUM_THREADS','one thread MKL_NUM_THREADS','one thread NUMEXPR_NUM_THREADS']:
 ck('recorded resource '+name,any(x['name']==name and x['passed']for x in c['checks']))
ck('fresh candidate absence record',fresh['candidate_absent']is True)
rehash(fresh['failed_files'])
attempts=[]
for tag in ['STATE_SHAPE','SCALAR_BATCH_REPLAY']:
 aj=read(V/('JOB_FAILED_'+tag+'.json'));ae=read(V/('EXIT_FAILED_'+tag+'.json'));am=read(V/('MANUFACTURES_FAILED_'+tag+'.json'))
 mapping={str(ROOT/'independent_code/run_angular_integrand_precision.py'):V/('WORKER_FAILED_'+tag+'.py'),str(V/'MANUFACTURES.json'):V/('MANUFACTURES_FAILED_'+tag+'.json'),str(V/'DESIGN_ACCEPTANCE.json'):V/('DESIGN_ACCEPTANCE_FAILED_'+tag+'.json')}
 for p,h in aj['bindings'].items():bind(mapping.get(p,p),h)
 for p in [V/('LOG_FAILED_'+tag+'.txt'),V/('DESIGN_ACCEPTANCE_FAILED_'+tag+'.json'),V/('DESIGN_ACCEPTANCE_FAILED_'+tag+'.md')]:bind(p)
 ck('failed nonzero '+tag,ae['returncode']!=0 and aj['utc']<ae['utc']<job['utc'])
 ck('historical manufacture57 '+tag,am['count']==len(am['checks'])==57 and all(x['passed']for x in am['checks']))
 # Each old manufacture source must map to the archived source, with all other dependencies stable.
 for p,h in am['bindings'].items():bind(mapping.get(p,p),h)
 attempts.append(dict(tag=tag,pid=aj['pid'],launch_utc=aj['utc'],exit=ae,scope='Historical wrapper PID and return-code record, no external process attestation.'))
old=Path(fresh['failed_directory']);replay=[]
for digits in [72,108]:
 total=0
 for kind in ['local','integrands']:
  olddir=old/f'R3_{kind}_{digits}';newdir=C/f'R3_{kind}_{digits}'
  oldpaths=sorted(olddir.glob('chunk_*.json.gz'));newpaths=sorted(newdir.glob('chunk_*.json.gz'))
  ck('same replay chunk names '+str((digits,kind)),[p.name for p in oldpaths]==[p.name for p in newpaths]and bool(oldpaths))
  for op,npth in zip(oldpaths,newpaths):
   oj=json.loads(gzip.decompress(bind(op)));nj=json.loads(gzip.decompress(bind(npth)))
   ck('attempt2/3 rows '+str((digits,kind,op.name)),oj['rows']==nj['rows']and oj['rows_sha256']==nj['rows_sha256'])
   total+=sum(len(row)for row in oj['rows'])
 replay.append(dict(digits=digits,equal_decimal_scalars=total,expected=5888+4))
 ck('complete replay scalar count '+str(digits),total==5892)
rounding=[]
for r in [3,30]:
 p=C/f'R{r}_geometry.npz';bind(p)
 with np.load(p,allow_pickle=False) as z:g={k:z[k]for k in z.files}
 x=F(float(g['x']));entries=[]
 for k,eps in enumerate([1e-5,1e-6]):
  maxima={name:dict(value=F(0),index=None)for name in ['abs_delta_plus','abs_delta_minus','abs_centre_shift','abs_relative_separation_error','delta_plus_over_ulp_xplus','delta_minus_over_ulp_xminus']}
  for i in range(len(g['node'])):
   h=F(float(g['h'][i,k]));xp=F(float(g['xplus'][i,k]));xm=F(float(g['xminus'][i,k]));ck('positive h '+str((r,k,i)),h>0)
   dp=xp-x-h;dm=xm-x+h
   vals=[abs(dp),abs(dm),abs(dp+dm)/2,abs(dp-dm)/(2*h),abs(dp)/F(math.ulp(float(xp))),abs(dm)/F(math.ulp(float(xm)))]
   for name,val in zip(maxima,vals):
    if maxima[name]['index']is None or val>maxima[name]['value']:maxima[name]=dict(value=val,index=i)
  entries.append(dict(epsilon=eps,maxima={name:dict(value=float(a['value']),exact=str(a['value']),index=a['index'],node=float(g['node'][a['index']]))for name,a in maxima.items()}))
 rounding.append(dict(radius=r,nodes=len(g['node']),entries=entries))
for p,h in list(bindings.items()):ck('end stable '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='PASS_SUPPLEMENT333_REVIEW_PENDING',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,display_observations=observations,failed_attempts=attempts,radius3_cross_attempt_replay=replay,rounded_coordinate_geometry=rounding,scope='Finite arithmetic/provenance/coordinate data only; no full-grid MP, derivative enclosure, primary endpoint or historical process attestation.')
(V/'SUPPLEMENT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in ['status','utc','count','display_observations','radius3_cross_attempt_replay']}))
