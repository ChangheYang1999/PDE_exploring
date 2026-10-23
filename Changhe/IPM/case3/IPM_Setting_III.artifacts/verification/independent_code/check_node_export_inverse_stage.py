"""Manufacture instrumented integration, exact decompositions and selector."""
from pathlib import Path
from datetime import datetime,timezone
import os,json,hashlib,time,traceback
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();start=datetime.now(timezone.utc).isoformat();tick=time.perf_counter()
paths=[Path(__file__),Path('independent_code/node_export_inverse_stage.py'),Path('independent_code/run_actual_node_inverse.py'),R/'CANDIDATE_INVERSE_EXECUTION_PROOF.md',R/'LOCAL_REGIONAL_BOUND_PROOF.md',R/'LOCAL_JET_REVIEW_RESOLUTION_PROOF.md',R/'INVERSE_RESTART_AND_REVIEW_PROOF.md',R/'INVERSE_STAGE_HAND_DENOMINATOR_CORRECTION.md',V/'PARTITION_CHECKS.json']+[Path('independent_code')/n for n in ['hydrostatic_power_tail.py','node_export_ratio_partition.py','independent_hydrostatic.py','node_export_high_basis_reference.py','node_export_arithmetic_strict.py','node_export_arithmetic.py']]
bindings={str(p):sha(p)for p in paths};checks=[];rows=[]
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
try:
 a=json.loads((V/'PARTITION_CHECKS.json').read_text());ck('881 preceding production manufactures',a['count']==len(a['checks'])==881 and all(z['passed']for z in a['checks']))
 for p,h in a['bindings'].items():ck('inherited '+p,sha(p)==h);bindings[p]=h
 import numpy as np
 from fractions import Fraction as F
 from node_export_inverse_stage import RULES,META,quadrature_parts,evaluate,panels,finite_arithmetic,select_witnesses,stability,maxima,discrepancy
 from node_export_high_basis_reference import slowjet,slow_reference
 from hydrostatic_power_tail import PowerVerticalInverse
 from node_export_ratio_partition import RatioPowerVerticalInverse,ratio_nodes
 from independent_hydrostatic import finite_nodes
 points=sorted({(row['x'],row['y'])for row in a['rows']})
 for x,y in points:
  for label,rule in RULES.items():
   got=evaluate(slowjet,x,y,.5,rule);cls=RatioPowerVerticalInverse if label=='C'else PowerVerticalInverse;old=cls(slowjet,.5,rule['order'],rule['tail_order'],rule['split'],rule['inner']).at(x,y)
   for k in ['V','Phi','dV2_dy','tail_V']:ck('predecessor identity '+str((x,y,label,k)),np.array_equal(got[k],old[k]))
   xx,yy,an,bn,tn,meta=quadrature_parts(x,y,.5,rule);ck('metadata shape/finite '+str((x,y,label)),len(meta)==len(META)and np.isfinite(meta).all()and meta[6]>0 and meta[7]>=0)
   ck('metadata rule counts '+str((x,y,label)),meta[3]==meta[1]*rule['order']and meta[4]==meta[2]*rule['order']and meta[5]==rule['tail_order'])
   fn=ratio_nodes if label=='C'else finite_nodes
   for lo,hi,z in [(0.,yy,an),(yy,meta[0],bn)]:
    zz,ww=fn(lo,hi,rule['order'],rule['inner']);ck('independent source node/weight identity '+str((x,y,label,lo)),np.array_equal(z[0],zz)and np.array_equal(z[1],ww))
   ref=slow_reference(x,y,meta[0],100)
   for name in ref:
    actual=meta[0]if name=='R_split'else got[name];a0,b0=np.atleast_1d(actual),np.atleast_1d(ref[name]);nz=b0!=0;ck('closed pure-relative '+str((x,y,label,name)),np.all(abs(a0[nz]-b0[nz])/abs(b0[nz])<2e-10)and np.all(a0[~nz]==0))
   rows.append(dict(x=x,y=y,rule=label,metadata=meta.tolist()))
 for kind in ['dyadic','ratio']:
  z,w,info=panels(1.,np.nextafter(1.,2.),64,.125,kind);ck('rounded endpoint explicit '+kind,len(z)==64 and np.all(w>0)and info['endpoint_nodes']>0 and info['min_width']>0)
  z,w,info=panels(0.,0.,64,.125,kind);ck('empty interval '+kind,len(z)==len(w)==info['nodes']==info['count']==0 and info['min_width']is None)
 rr,dd=finite_arithmetic([1.,2.,-3.],[.5,1.,4.],[2.,3.],[-1.,5.],[6.,-2.],2.,.25,.75)
 # Hand: R=(.5+2)*2+(1.5+3)*(-3)-1=-9.5; Nf=19.5; Nv=7.75.
 ck('hand exact residual',np.array_equal(rr[:3],np.array([-9.5,19.5,7.75])))
 ck('both references have correct signed telescope',np.array_equal(dd[:,4],dd[:,2]+dd[:,3])and np.array_equal(dd[:,4],dd[:,6]+dd[:,7]))
 rr,dd=finite_arithmetic([0.,0.,1.],[0.,0.,1.],[3.,0.],[2.,0.],[1.,0.],2.,1.,0.)
 ck('axis undefined denominator ratios',np.array_equal(rr[:3],[0.,0.,0.])and np.isnan(rr[3:]).all())
 disc,zeros=discrepancy(np.array([0.,1.,-1.]),np.array([0.,-1.,1.]));ck('pure metric zero and opposite signs',zeros==1 and np.array_equal(disc['pure_relative'],[0.,2.,2.]))
 # 2304 synthetic nodes provide an independently calculable selection exercise.
 n=2304;x=np.ones(n);y=np.arange(n,dtype=float)/100;own=np.tile([1.,2.,3.,4.],(n,1));prod=own[:,:3].copy();vm=np.zeros((n,2));vp=np.ones((n,2));arr=np.zeros((n,5));arr[:,1:3]=1.;A=dict(velocity=np.zeros((n,2)),residual=arr.copy());B=dict(velocity=np.zeros((n,2)),residual=arr.copy());A['velocity'][17,0]=7.;B['velocity'][19,1]=-3.;A['residual'][25,[0,3,4]]=5.;B['residual'][31,[0,3,4]]=4.;proxy=np.zeros(n);proxy[53]=8.;own[59,3]=12.
 sel=select_witnesses(x,y,own,prod,vm,vp,A,B,[11],proxy)
 ck('witness ties and selection probes',{0,11,17,19,25,31,53,59,1139,2294,2296}<=set(sel['indices']),sel['indices'])
 ck('source tie explicit index zero','exact absolute map-jet residual contribution'in sel['reasons']['0']and'exact relative map-jet residual contribution'in sel['reasons']['0'])
 ck('witness sorted unique and source counts',sel['indices']==sorted(set(sel['indices']))and sel['map_residual_sign_disagreement_count']==0 and sel['map_residual_both_zero_count']==0)
 st=stability([1.,1.,1.],[0.,0.],[[1.,1.],[1.,1.],[1.,1.]],2.,1.,1.);ck('identical rules stable',st['empirical_stable']and st['S']==0 and not st['zero_D'])
 st=stability([1.,1.,1.],[0.,0.],[[1.,1.],[1.,1.],[1.1,1.]],2.,1.,1.);ck('resolved spread failure remains failure',not st['empirical_stable']and st['S']>0)
 st=stability([0.,0.,1.],[0.,0.],[[0.,0.]]*3,2.,1.,0.);ck('zero denominator remains undefined',not st['empirical_stable']and st['zero_Nf']and st['spread_over_Nf_B']is None and st['zero_D'])
 st=stability([5.,1.,1.],[0.,0.],[[.5+1e-12,.5],[.5,.5],[.5,.5]],2.,1.,1.);ck('zero B residual additional criterion undefined',st['zero_R_B']and st['spread_over_abs_R_B']is None and st['within_one_percent_of_abs_R_B']is None)
 st=stability([1.,1.,0.],[0.,0.],[[1.,1.],[1.,2.],[1.,3.]],2.,1.,1.);ck('orthogonal velocity spread explicit',st['S']==0 and any(z['component']==2 and z['absolute']>0 for z in st['component_spreads']))
 ck('criterion is explicitly map relative',st['criterion_label']=='map-discrepancy-relative only')
 for p,h in bindings.items():ck('stable '+p,sha(p)==h)
 out=dict(status='PASS_INSTRUMENTED_INVERSE_AND_SELECTION',started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_monotonic_seconds=time.perf_counter()-tick,count=len(checks),checks=checks,bindings=bindings,rows=rows,scope='Finite manufacture and selector tests before candidate inverse execution; primary unresolved.')
 (V/'INVERSE_STAGE_MANUFACTURES.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks),out['elapsed_monotonic_seconds'])
except Exception:
 (V/'INVERSE_STAGE_MANUFACTURES_FAILURE.json').write_text(json.dumps(dict(started_utc=start,failed_utc=datetime.now(timezone.utc).isoformat(),checks=checks,bindings=bindings,traceback=traceback.format_exc()),indent=2)+'\n');raise
