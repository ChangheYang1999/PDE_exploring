"""Sole-heavy resumable all-node auxiliary inverse comparison. No producer code."""
from pathlib import Path
from datetime import datetime,timezone
import os,json,hashlib,time,traceback
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';OUT=V/'candidate_inverse';OUT.mkdir(exist_ok=True)
now=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
start=now();tick=time.perf_counter();bindings={};checks=[]
def ck(name,ok,evidence=None):
 checks.append(dict(name=name,passed=bool(ok),evidence=evidence))
 if not ok:raise AssertionError((name,evidence))
def bind(p,h=None):
 p=Path(p).resolve().relative_to(Path.cwd());z=sha(p)
 if str(p)in bindings:ck('consistent repeated binding '+str(p),bindings[str(p)]==z)
 ck('binding '+str(p),h is None or h==z);bindings[str(p)]=z;return p
def jsave(p,d):
 tmp=p.with_suffix(p.suffix+'.tmp');tmp.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n');tmp.replace(p)
def gate(name,status,count=None):
 p=bind(V/name);d=json.loads(p.read_text());ck('completed gate '+name,d['status']==status and d['count']==len(d['checks'])and all(x['passed']for x in d['checks'])and(count is None or d['count']==count))
 for p,h in d['bindings'].items():bind(p,h)
 return d
try:
 for p in [__file__,'independent_code/node_export_inverse_stage.py','independent_code/node_export_checkpoint.py','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py','independent_code/independent_hydrostatic.py','independent_code/node_export_arithmetic_strict.py','independent_code/node_export_arithmetic.py',R/'CANDIDATE_INVERSE_EXECUTION_PROOF.md',R/'LOCAL_REGIONAL_BOUND_PROOF.md',R/'LOCAL_JET_REVIEW_RESOLUTION_PROOF.md',R/'INVERSE_RESTART_AND_REVIEW_PROOF.md']:bind(p)
 a=gate('ACTUAL_JETS.json','PASS_ACTUAL_NODE_JETS_AND_EXACT_FIXED_MAP_ARITHMETIC',2468)
 gate('ACTUAL_MP_JETS.json','PASS_ACTUAL_LOCAL_MP_JET_WITNESSES',183)
 gate('INVERSE_STAGE_MANUFACTURES.json','PASS_INSTRUMENTED_INVERSE_AND_SELECTION')
 gate('INVERSE_RESTART_MANUFACTURES.json','PASS_PHASE_RESTART_AND_TAMPER_REJECTION')
 # The design review is an explicit launch gate, created only after disagreements close.
 design=json.loads(bind(V/'INVERSE_DESIGN_ACCEPTANCE.json').read_text());ck('actual reviewed design',design['status']=='ACCEPTED_FOR_FINITE_COMPUTATION')
 for p,h in design['bindings'].items():bind(p,h)
 import numpy as np
 import torch
 from q_local_checkpoint import QLocalCheckpoint
 from independent_hydrostatic import CartesianQJet
 from node_export_checkpoint import PhaseStore,write_or_validate_selection
 from node_export_inverse_stage import masks,RULES,META,RESIDUAL_COLUMNS,DECOMP_COLUMNS,evaluate,finite_arithmetic,maxima,select_witnesses,stability
 torch.set_num_threads(1)
 source=json.loads((V/'PROVENANCE_INPUTS.json').read_text());state=bind(source['state']['frozen'],'4ad484e6391001597ab57d501c8b3f644259af7b4c217b5032a28b00be609d01')
 bind(V/'source_nodes_maps.npz','071b990c7a9ee3a91faeca5a1cc8c7d9ef6ef478f41ccd591fbe1ad5575d42d7')
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(state)
 with np.load(V/'actual_node_jets.npz',allow_pickle=False)as f:d={k:f[k]for k in f.files}
 with np.load(V/'source_nodes_maps.npz',allow_pickle=False)as f:s={k:f[k]for k in f.files}
 x,y=d['X'],d['Y'];own,prod=d['own_jet'],d['producer_jet'];vm=np.column_stack([s['V1_map'],s['V2_map']]);vp=np.column_stack([s['V1_ref'],s['V2_ref']]);jet=CartesianQJet(q).jet
 ck('exact state parameters',q.N==96 and q.M==24 and q.cl==2 and q.kappa==2 and q.L==1 and q.p==.5)
 ck('reviewed17 MP witnesses',a['mp_witness_indices']==[0,4,11,23,767,1128,1139,1151,1747,2136,2160,2261,2263,2277,2280,2291,2303])
 ck('four region counts',[int(mask.sum())for mask in masks(x,y)]==[480,768,720,336])
 ck('region index mapping',all(np.array_equal(np.flatnonzero(mask),np.arange(lo,hi))for mask,(lo,hi)in zip(masks(x,y),[(0,480),(480,1248),(1248,1968),(1968,2304)])))
 ck('target coordinate identity',np.array_equal(x,s['X'])and np.array_equal(y,s['Y'])and len(x)==2304)
 basebindings=dict(bindings)
 def run_phase(label,indices,selection=None):
  phasebindings=dict(basebindings)
  if selection is not None:phasebindings[str(selection)]=sha(selection)
  columns=dict(metadata=META,residual=RESIDUAL_COLUMNS,decomposition=DECOMP_COLUMNS,decomposition_references=['Vm','Vp'])
  store=PhaseStore(OUT/(label+'.npz'),label,indices,RULES[label],phasebindings,columns)
  def compute(i):
   z=evaluate(jet,float(x[i]),float(y[i]),q.p,RULES[label]);rr,dd=finite_arithmetic(own[i],prod[i],z['V'],vm[i],vp[i],q.cl,x[i],y[i])
   row=dict(velocity=z['V'],Phi=z['Phi'],dV2dy=z['dV2_dy'],tail_velocity=z['tail_V'],metadata=z['meta'],residual=rr,decomposition=dd)
   if any(not np.isfinite(val).all()for name,val in row.items()if name!='residual')or not np.isfinite(rr[:3]).all():raise ArithmeticError('nonfinite integral/arithmetic')
   return row
  return store.run(compute,lambda done,i:print('PHASE',label,done,'of',len(indices),'node',i,now(),flush=True))
 A=run_phase('A',np.arange(2304));B=run_phase('B',np.arange(2304))
 h=np.maximum(1.,np.hypot(x,y))*2**-10
 fd=(-q.rho(x+2*h,y)+16*q.rho(x+h,y)-30*q.rho(x,y)+16*q.rho(x-h,y)-q.rho(x-2*h,y))/(12*h*h)
 proxy=abs(own[:,3]-fd);ck('finite FD proxy',np.isfinite(proxy).all())
 selection=select_witnesses(x,y,own,prod,vm,vp,A,B,a['mp_witness_indices'],proxy)
 ck('exact jet contribution indices',selection['absolute_jet_argmax']==2296 and selection['relative_jet_argmax']==2294)
 ck('exact sign and zero counts',selection['map_residual_sign_disagreement_count']==4 and selection['map_residual_both_zero_count']==0)
 selection.update(generated_utc=now(),bindings={str(OUT/'A.npz'):sha(OUT/'A.npz'),str(OUT/'B.npz'):sha(OUT/'B.npz')},FD_proxy_step='h=2^-10 max(1,r)',FD_proxy_max=float(max(proxy)),FD_proxy_index=int(np.argmax(proxy)),FD_proxy_x=float(x[np.argmax(proxy)]),FD_proxy_y=float(y[np.argmax(proxy)]),FD_proxy_radius=float(np.hypot(x[np.argmax(proxy)],y[np.argmax(proxy)])),FD_proxy_scope='Selection only; not second-derivative error estimate')
 selpath=OUT/'SELECTION.json'
 write_or_validate_selection(selpath,selection)
 C=run_phase('C',selection['indices'],selpath)
 exact_identity_count=0
 for label,data in [('A',A),('B',B),('C',C)]:
  for k,i in enumerate(data['indices']):
   rr,dd=finite_arithmetic(own[i],prod[i],data['velocity'][k],vm[i],vp[i],q.cl,x[i],y[i])
   if not np.array_equal(rr,data['residual'][k],equal_nan=True)or not np.array_equal(dd,data['decomposition'][k]):raise ArithmeticError('stored arithmetic mismatch '+str((label,int(i))))
   exact_identity_count+=4
  ck('rechecked all exact stored arithmetic '+label,True,len(data['indices']))
 comparisons=[]
 for j,i in enumerate(selection['indices']):
  z=stability(own[i],vm[i],[A['velocity'][i],B['velocity'][i],C['velocity'][j]],q.cl,x[i],y[i]);z.update(index=i,x=float(x[i]),y=float(y[i]));comparisons.append(z)
 newmp=sorted(set(selection['indices'])-set(a['mp_witness_indices']))
 summaries={label:maxima(x,y,z['residual'])for label,z in [('A',A),('B',B)]}
 mpintegrand=sorted({row['metrics']['absR']['index']for row in summaries['B']}|{1139})
 for p,h in basebindings.items():ck('stable '+p,sha(p)==h)
 artifacts={str(OUT/n):sha(OUT/n)for n in ['A.npz','B.npz','C.npz','SELECTION.json']}
 output=dict(status='COMPLETE_FINITE_RULES_REQUIRES_LOCAL_MP_INTEGRAND_MP_AND_FINAL_REVIEW',started_utc=start,finished_utc=now(),elapsed_monotonic_seconds=time.perf_counter()-tick,count=len(checks),checks=checks,bindings=basebindings,artifacts=artifacts,rule_sizes={'A':2304,'B':2304,'C':len(selection['indices'])},exact_identity_count=exact_identity_count,summaries=summaries,stability=comparisons,empirical_stability_pass_count=sum(z['empirical_stable']for z in comparisons),new_local_mp_indices=newmp,mp_integrand_indices=mpintegrand,scope='Auxiliary hydrostatic inverse, not full-plane IPM. Fixed finite rule arithmetic only. New local MP, MP integrand and final review pending; tail_V components are unimposed raw sums; true inverse error uncertified; historical maps open; primary unresolved.')
 jsave(OUT/'RULES_COMPLETE.json',output);print(output['status'],now(),flush=True)
except Exception:
 jsave(OUT/'FAILURE.json',dict(utc=now(),started_utc=start,checks=checks,bindings=bindings,traceback=traceback.format_exc()));raise
