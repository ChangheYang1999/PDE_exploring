"""Audit saved tail-sum algebra independently of the tail generator."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,math,hashlib,os,copy,sys
if sys.flags.optimize:raise SystemExit("verification refuses optimized Python")
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
import numpy as np
R=Path('research/hydrostatic_tail_rule_provenance');V=R/'verification';checks=[];bindings={}
now=lambda:datetime.now(timezone.utc).isoformat()
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def identity_accepts(current,expected,prior):return (expected is None or current==expected) and (prior is None or current==prior)
def bind(p,h=None):
 p=Path(p).resolve();p.relative_to(Path.cwd().resolve());s=hashlib.sha256(p.read_bytes()).hexdigest();ck('binding '+str(p),identity_accepts(s,h,bindings.get(str(p))));bindings[str(p)]=s;return p
def scalar_record(row):
 nf=row['export_Nf'];assert math.isfinite(nf)and nf>0
 assert [z['n']for z in row['rules']]==[200,400,800,1600]
 y,gx,gy=map(F,[row['y'],row['jet'][1],row['jet'][2]])
 for z in row['rules']:
  for key in ['q2','q3']:
   a=z[key];assert set(a)=={'value','absolute_sum','endpoint_coincident_count'}
   assert len(a['value'])==len(a['absolute_sum'])==2 and all(math.isfinite(x)for x in a['value']+a['absolute_sum'])
   assert all(abs(x)<=v for x,v in zip(a['value'],a['absolute_sum']))
   assert type(a['endpoint_coincident_count'])is int and 0<=a['endpoint_coincident_count']<=z['n']
  ix,ixx=[F(a)-F(b)for a,b in zip(z['q2']['value'],z['q3']['value'])]
  true={'deltaV1':-ix,'deltaV2':y*ixx,'deltaR':-gx*ix+y*gy*ixx};saved=z['delta_q2_minus_q3']
  assert {k:F(v)for k,v in saved['exact'].items()}==true
  assert all(saved[k]==float(v)for k,v in true.items())
  assert saved['deltaR_over_export_Nf']==float(abs(true['deltaR'])/F(nf))
  assert len(z['conditioning'])==2
  for k,out in enumerate(z['conditioning']):
   diff=abs(F(z['q2']['value'][k])-F(z['q3']['value'][k]));scale=(F(z['q2']['absolute_sum'][k])+F(z['q3']['absolute_sum'][k]))/2**52
   assert F(out['exact_difference'])==diff and F(out['exact_scale'])==scale
   if scale:assert out['status']=='FINITE_CONDITIONING_SCALE_ONLY'and out['ratio']==float(diff/scale)
   else:assert not diff and out['status']=='UNDEFINED_ZERO_SUM'and out['ratio']is None
 for k,sp in enumerate(row['q2_empirical_spread']):
  values=[F(z['q2']['value'][k])for z in row['rules']];exact=max(values)-min(values);assert F(sp['exact'])==exact and sp['value']==float(exact)
def manufacture():
 ck('identity permits first binding',identity_accepts('a',None,None))
 ck('identity permits stable alias',identity_accepts('a','a','a'))
 ck('identity rejects changed prior',not identity_accepts('b',None,'a'))
 ck('identity rejects wrong expected',not identity_accepts('a','b',None))
 ck('identity resolves relative absolute alias',Path(__file__).resolve()==Path.cwd().joinpath(__file__).resolve())
 def make():
  vals=[1.,2.];s=dict(value=vals,absolute_sum=vals,endpoint_coincident_count=0);zero=dict(ratio=0.,status='FINITE_CONDITIONING_SCALE_ONLY',exact_difference='0',exact_scale='1/2251799813685248')
  out=dict(index=0,x=1.,y=2.,jet=[1.,3.,1.,2.],export_Nf=4.,rules=[],q2_empirical_spread=[dict(exact='0',value=0.),dict(exact='0',value=0.)])
  for n in [200,400,800,1600]:out['rules'].append(dict(n=n,q2=copy.deepcopy(s),q3=copy.deepcopy(s),conditioning=[copy.deepcopy(zero),dict(zero,exact_scale='1/1125899906842624')],delta_q2_minus_q3=dict(deltaV1=0.,deltaV2=0.,deltaR=0.,exact=dict(deltaV1='0',deltaV2='0',deltaR='0'),deltaR_over_export_Nf=0.)))
  return out
 z=make();scalar_record(z);ck('synthetic identical sums',True)
 for name,modify in [('exact corruption',lambda z:z['rules'][0]['delta_q2_minus_q3']['exact'].update(deltaR='1')),('rounded corruption',lambda z:z['rules'][0]['delta_q2_minus_q3'].update(deltaV1=1.)),('wrong rule order',lambda z:z['rules'].reverse()),('negative Nf',lambda z:z.update(export_Nf=-1.)),('bad conditioning',lambda z:z['rules'][0]['conditioning'][0].update(ratio=1.)),('bad spread',lambda z:z['q2_empirical_spread'][0].update(exact='1')),('bad endpoint count',lambda z:z['rules'][0]['q3'].update(endpoint_coincident_count=-1)),('nonfinite sum',lambda z:z['rules'][0]['q2']['value'].__setitem__(0,math.inf))]:
  z=make();modify(z)
  try:scalar_record(z)
  except(AssertionError,ValueError,OverflowError):ck('reject '+name,True)
  else:raise AssertionError(name)
 # Nonzero component changes with exact cancellation in the residual.
 z=make()
 for q in z['rules']:
  q['q3']=dict(value=[3.,5.],absolute_sum=[3.,5.],endpoint_coincident_count=0)
  q['delta_q2_minus_q3']=dict(deltaV1=2.,deltaV2=-6.,deltaR=0.,exact=dict(deltaV1='2',deltaV2='-6',deltaR='0'),deltaR_over_export_Nf=0.)
  q['conditioning']=[dict(status='FINITE_CONDITIONING_SCALE_ONLY',exact_difference='2',exact_scale=str(F(4,2**52)),ratio=float(F(2)*2**52/4)),dict(status='FINITE_CONDITIONING_SCALE_ONLY',exact_difference='3',exact_scale=str(F(7,2**52)),ratio=float(F(3)*2**52/7))]
 scalar_record(z);ck('nonzero velocity changes cancel',True)
 for row in z['rules']:
  for key in ['q2','q3']:row[key].update(value=[0.,0.],absolute_sum=[0.,0.])
  row['conditioning']=[dict(status='UNDEFINED_ZERO_SUM',ratio=None,exact_difference='0',exact_scale='0')for _ in range(2)]
  row['delta_q2_minus_q3']=dict(deltaV1=0.,deltaV2=0.,deltaR=0.,exact=dict(deltaV1='0',deltaV2='0',deltaR='0'),deltaR_over_export_Nf=0.)
 scalar_record(z);ck('zero conditioning explicitly undefined',True)
def main():
 manufacture();manufacture_count=len(checks);d=json.loads(bind(V/'CHECKS.json').read_text());ck('actual stage finite PASS',d['status']=='PASS_FINITE_SELECTED_TAIL_RULES_REQUIRES_FINAL_REVIEW'and d['count']==len(d['checks'])and all(z['passed']for z in d['checks']))
 for p,h in d['bindings'].items():bind(p,h)
 e=json.loads(bind(V/'TAIL_EXECUTION_RESULT.json').read_text());ck('successful ceased execution',e['returncode']==0 and all(not Path('/proc',str(e[k])).exists()for k in ['wrapper_pid','timeout_pid']))
 base=Path('research/new_node_export_record_audit/verification');cfg=json.loads(bind(base/'EXPORT_INPUTS.json').read_text())['states'][0];prev=json.loads(bind(base/'CHECKS.json').read_text())['states'][0]
 ck('frozen S160',cfg['tag']==prev['tag']=='S160'and cfg['N']==160 and cfg['M']==40);bind(cfg['state'],cfg['state_sha256'])
 with np.load(bind(cfg['export'],cfg['export_sha256']),allow_pickle=False)as z:arr={k:z[k]for k in z.files}
 ck('same selected row order',[z['index']for z in d['rows']]==prev['selected_jet_indices']and len(d['rows'])==12)
 for row in d['rows']:
  i=row['index'];ck('exact export coordinates and operands '+str(i),all(row[k]==float(arr[j][i])for k,j in [('x','x'),('y','y'),('export_Rh','R_h'),('export_Nf','N_f')]))
  ck('axis flags '+str(i),row['axis']==dict(x_zero=row['x']==0,y_zero=row['y']==0));scalar_record(row);ck('all recorded finite algebra '+str(i),True)
 summary=[]
 for n in [200,400,800,1600]:
  rows=[(row,next(z for z in row['rules']if z['n']==n))for row in d['rows']];a=max(rows,key=lambda p:p[1]['delta_q2_minus_q3']['deltaR_over_export_Nf']);b=max(rows,key=lambda p:abs(p[1]['delta_q2_minus_q3']['deltaR']))
  summary.append(dict(n=n,selected_rows=len(rows),normalized_argmax=a[0]['index'],max_abs_deltaR_over_export_Nf=a[1]['delta_q2_minus_q3']['deltaR_over_export_Nf'],absolute_argmax=b[0]['index'],max_abs_deltaR=abs(b[1]['delta_q2_minus_q3']['deltaR']),q3_endpoint_coincident_counts=sorted({z['q3']['endpoint_coincident_count']for _,z in rows})))
 for p in [__file__,R/'FINAL_SELECTED_ALGEBRA_PROOF.md',R/'SELECTED_FINAL_GUARD_RESOLUTION_PROOF.md',V/'TAIL_JOB.json']:bind(p)
 original=json.loads(bind(V/'FINAL_SELECTED_CHECKS.json').read_text());ck('summary exactly agrees with original final arithmetic',summary==original['summary'])
 out=dict(status='PASS_FINITE_SELECTED_TAIL_ALGEBRA_REQUIRES_RESULT_REVIEW',utc=now(),interpreter_flags=dict(optimize=sys.flags.optimize,repr=repr(sys.flags)),count=len(checks),manufacture_count=manufacture_count,checks=checks,bindings=bindings,summary=summary,scope='Recorded finite-sum algebra only. No independent replay of candidate tail integrands, no error enclosure, no historical causality, no all-node maximum, no primary endpoint.')
 (V/'FINAL_SELECTED_CHECKS_V2.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],manufacture_count,out['utc'])
if __name__=='__main__':main()
