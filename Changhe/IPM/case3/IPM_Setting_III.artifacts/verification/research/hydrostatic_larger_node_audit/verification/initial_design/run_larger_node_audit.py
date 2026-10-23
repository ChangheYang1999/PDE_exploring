"""Single-thread, sole-heavy finite auxiliary node audit. No producer imports."""
from pathlib import Path
from datetime import datetime,timezone
import os,json,hashlib,time,traceback,sys
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
R=Path('research/hydrostatic_larger_node_audit');V=R/'verification';O=V/'candidate';O.mkdir(exist_ok=True)
now=lambda:datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();start=now();tick=time.perf_counter();checks=[];bindings={}
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e));assert b,(n,e)
def bind(p,h=None):
 p=str(p);hh=sha(p);ck('binding '+p,(h is None or h==hh)and(p not in bindings or bindings[p]==hh));bindings[p]=hh;return Path(p)
def savejson(p,d):
 t=p.with_suffix('.tmp');t.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n');t.replace(p)
try:
 for p in [__file__,'independent_code/larger_node_stage.py','independent_code/node_export_inverse_stage.py','independent_code/independent_hydrostatic.py','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py',R/'PROOF.md',R/'SOURCE_EQUIVALENCE_PROOF.md']:bind(p)
 accept=json.loads(bind(V/'DESIGN_ACCEPTANCE.json').read_text());ck('accepted actual design',accept['status']=='ACCEPTED_FOR_FINITE_COMPUTATION')
 for p,h in accept['bindings'].items():bind(p,h)
 inp=json.loads(bind(V/'INPUTS.json').read_text())
 for x in inp['files']+inp['states']+[inp['full224']]:bind(x['path'],x['sha256'])
 import numpy as np
 import torch
 import larger_node_stage,node_export_inverse_stage,independent_hydrostatic,q_local_checkpoint,q_checkpoint_reader
 from larger_node_stage import coordinates,rounded_fields,summaries,selection,pair_spreads,NodeStore
 from node_export_inverse_stage import RULES,evaluate,META
 from q_local_checkpoint import QLocalCheckpoint
 from independent_hydrostatic import CartesianQJet
 torch.set_num_threads(1)
 for m in [larger_node_stage,node_export_inverse_stage,independent_hydrostatic,q_local_checkpoint,q_checkpoint_reader]:ck('own module path '+m.__name__,Path(m.__file__).resolve().parent==Path('independent_code').resolve())
 base=dict(bindings);results=[];artifacts={}
 for state in inp['states']:
  N=state['N'];tag='N'+str(N)
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(state['path'])
  ck('exact dimensions '+tag,q.N==N and q.M==state['M']);ck('exact parameters '+tag,q.cl==2 and q.kappa==2 and q.L==1 and q.p==.5 and q.basis=='local'and q.meta['basis_nodes_source']=='stored')
  ck('finite coefficients '+tag,np.isfinite(q.u).all())
  full=q
  if N==224:
   with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):full=QLocalCheckpoint(inp['full224']['path'])
   ck('raw full defining equivalence '+tag,np.array_equal(full.u,q.u)and np.array_equal(full.tk,q.tk)and all(getattr(full,k)==getattr(q,k)for k in ['N','M','basis','L','cl','kappa','p']))
  ck('M-row convention '+tag,not bool((full.data.get('result')or{}).get('fine',False))and not bool((full.data.get('inverse_options')or{}).get('fine',False)))
  xy=coordinates(q);expected=q.N*q.M;ck('positive finite node count '+tag,xy.shape==(expected,2)and np.isfinite(xy).all()and(xy>0).all())
  rr=np.hypot(xy[:,0],xy[:,1]);t,ss,ww=q.coordinates(rr);src=np.repeat(q.tk[1:],q.M);ck('scalar compactification inverse '+tag,np.max(abs(t-src))<2e-14)
  cj=CartesianQJet(q);j=np.vstack([cj.jet(xy[k:k+512,0],xy[k:k+512,1])for k in range(0,expected,512)]);ck('finite local jets '+tag,j.shape==(expected,4)and np.isfinite(j).all())
  ix=np.unique([0,expected//2,expected-1]);mirror=cj.jet(-xy[ix,0],-xy[ix,1]);ck('Cartesian parity '+tag,np.array_equal(mirror,j[ix]*np.array([-1,1,1,-1])))
  # A different polynomial evaluator reconstructs density at these same three points.
  direct=q.rho(xy[ix,0],xy[ix,1]);ck('Clenshaw density corroboration '+tag,np.all(abs(direct-j[ix,0])<=5e-12*np.maximum(1,abs(j[ix,0]))))
  target=O/(tag+'_targets.npz')
  if target.exists():
   with np.load(target,allow_pickle=False)as a:ck('unchanged targets '+tag,set(a.files)=={'xy','jets'}and np.array_equal(a['xy'],xy)and np.array_equal(a['jets'],j))
  else:
   tmp=target.with_suffix('.tmp')
   with tmp.open('wb')as a:np.savez_compressed(a,xy=xy,jets=j)
   tmp.replace(target)
  bb=dict(base);bb[str(target)]=sha(target)
  def phase(rule,ids,sp=None):
   pb=dict(bb)
   if sp is not None:pb[str(sp)]=sha(sp)
   store=NodeStore(O/(tag+'_'+rule+'.npz'),tag+'_'+rule,ids,xy,j,RULES[rule],pb)
   def compute(i):
    z=evaluate(cj.jet,*xy[i],q.p,RULES[rule]);return dict(velocity=z['V'],Phi=z['Phi'],dV2dy=z['dV2_dy'],tail_velocity=z['tail_V'],metadata=z['meta'],residual=rounded_fields(*xy[i],j[i],z['V'],q.cl))
   return store.run(compute,lambda done,i:print(tag,rule,done,'/',len(ids),i,now(),flush=True))
  B=phase('B',np.arange(expected))
  h=np.maximum(1,rr)*2**-10
  fd=(-q.rho(xy[:,0]+2*h,xy[:,1])+16*q.rho(xy[:,0]+h,xy[:,1])-30*q.rho(xy[:,0],xy[:,1])+16*q.rho(xy[:,0]-h,xy[:,1])-q.rho(xy[:,0]-2*h,xy[:,1]))/(12*h*h)
  proxy=abs(j[:,3]-fd);ck('finite FD selector '+tag,np.isfinite(proxy).all());sel=selection(xy,j,B,proxy);sel.update(B_sha256=sha(O/(tag+'_B.npz')),target_sha256=sha(target),proxy_step='2^-10 max(1,r)',scope='Selection only, not gxx error bound');sp=O/(tag+'_SELECTION.json')
  if sp.exists():ck('unchanged selection '+tag,json.loads(sp.read_text())==sel)
  else:savejson(sp,sel)
  ids=sel['indices'];A=phase('A',ids,sp);C=phase('C',ids,sp);comp=[]
  for pos,i in enumerate(ids):
   d=pair_spreads(xy[i],j[i],[A['velocity'][pos],B['velocity'][i],C['velocity'][pos]]);d.update(index=i,x=float(xy[i,0]),y=float(xy[i,1]));comp.append(d)
  # All saved row arithmetic is recomputed in this driver; a separately written final checker remains required.
  for name,data,idxs in [('B',B,range(expected)),('A',A,ids),('C',C,ids)]:
   for pos,i in enumerate(idxs):
    if not np.array_equal(data['residual'][pos],rounded_fields(*xy[i],j[i],data['velocity'][pos],q.cl),equal_nan=True):raise ArithmeticError('stored residual mismatch '+str((tag,name,i)))
   ck('all stored row arithmetic '+tag+name,True,len(idxs))
  sums=summaries(xy,B['residual']);mp_ids=sorted({z['index']for r in sums for z in r['metrics'].values()if z['index']is not None});globalrf=max((z for r in sums for k,z in r['metrics'].items()if k=='Rf'and z['index']is not None),key=lambda z:z['value'])['index']
  result=dict(N=N,M=q.M,points=expected,source=state,region_summaries=sums,selected=sel,comparisons=comp,local_mp_indices=mp_ids,integrand_mp_indices=[globalrf],producer_solver_nodes_Fmax=(full.data.get('result')or{}).get('nodes_Fmax'),producer_solver_nodes_Fmax_scope='Unverified diagnostic metadata; may include normalization rows',metadata_columns=META,status='FINITE_B_AND_SELECTED_AC_REQUIRES_MP_AND_FINAL_REVIEW')
  savejson(O/(tag+'_COMPLETE.json'),result);results.append(result)
  for p in [target,sp]+[O/(tag+'_'+label+'.npz')for label in ['A','B','C']]+[O/(tag+'_COMPLETE.json')]:artifacts[str(p)]=sha(p)
  print('STATE COMPLETE',tag,now(),flush=True)
 for p,h in base.items():ck('stable '+p,sha(p)==h)
 out=dict(status='COMPLETE_FINITE_LARGER_NODES_REQUIRES_MP_AND_FINAL_REVIEW',started_utc=start,finished_utc=now(),elapsed_seconds=time.perf_counter()-tick,count=len(checks),checks=checks,bindings=base,artifacts=artifacts,results=results,scope='Reconstructed collocation coordinates, finite hydrostatic quadrature; no exact-inverse error enclosure, historical authentication or full-plane IPM endpoint.')
 savejson(O/'COMPLETE.json',out);print(out['status'],now(),flush=True)
except Exception:
 savejson(O/'FAILURE.json',dict(utc=now(),started_utc=start,count=len(checks),checks=checks,bindings=bindings,traceback=traceback.format_exc()));raise
