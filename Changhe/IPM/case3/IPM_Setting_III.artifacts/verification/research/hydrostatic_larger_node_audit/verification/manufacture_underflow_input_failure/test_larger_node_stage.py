from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import os,json,hashlib,ast,math,traceback
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
import numpy as np
from larger_node_stage import NodeStore,SHAPES,exact_fields,rounded_fields,summaries,selection,pair_spreads,coordinates
from node_export_inverse_stage import evaluate,RULES
R=Path('research/hydrostatic_larger_node_audit');V=R/'verification';checks=[];bindings={};sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b):checks.append(dict(name=n,passed=bool(b)));assert b,n
def bind(p,h=None):
 p=str(p);hh=sha(p);ck('binding '+p,h is None or hh==h);bindings[p]=hh
try:
 for p in [__file__,'independent_code/larger_node_stage.py','independent_code/run_larger_node_audit.py','independent_code/node_export_inverse_stage.py','independent_code/independent_hydrostatic.py','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py',R/'PROOF.md',R/'SOURCE_EQUIVALENCE_PROOF.md',R/'HAND_NORMALIZATION_CORRECTION_PROOF.md',R/'DESIGN_REVIEW_RESOLUTION_PROOF.md',V/'INPUTS.json']:bind(p)
 for p in ['independent_code/larger_node_stage.py','independent_code/run_larger_node_audit.py']:ast.parse(Path(p).read_text());ck('Python parse '+p,True)
 # Independent hand arithmetic: a=20,b=-33,g=4 gives R=-17,Nf=57,Nv=16.
 ck('hand transport',exact_fields(1,2,[4,5,-3,0],[2,7])==[F(-17),F(57),F(16),F(17,57),F(17,16)])
 ck('zero denominators',exact_fields(0,0,[0,0,0,0],[0,0])==[F(0),F(0),F(0),None,None])
 xy=np.array([[.01,.02],[.02,.03],[.1,.2],[1.,2.],[100.,200.]]);jj=np.zeros((5,4));vv=np.zeros((5,2));rr=np.array([rounded_fields(*a,b,c)for a,b,c in zip(xy,jj,vv)])
 ss=summaries(xy,rr);ck('all undefined ratios count',sum(r['metrics']['Rf']['undefined_count']for r in ss)==5)
 empty=summaries(np.empty((0,2)),np.empty((0,5)));ck('empty regions',all(r['count']==0 and all(x['index']is None for x in r['metrics'].values())for r in empty))
 tie=rr.copy();tie[:,0]=1;ck('first exact tie',summaries(xy,tie)[0]['metrics']['absR']['index']==0)
 # g=y e^-y^2/(1+x^2): independently integrated vertical moments.
 def jet(x,y):
  x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));a=1+x*x;e=np.exp(-y*y)
  return np.stack([y*e/a,-2*x*y*e/a**2,(1-2*y*y)*e/a,(6*x*x-2)*y*e/a**3],axis=-1)
 for tag,rule in RULES.items():
  for x,y in [(0.,0.),(.25,.4),(1.,2.),(-.5,.8),(.3,-.7)]:
   z=evaluate(jet,x,y,.5,rule);a=1+x*x;b=(6*x*x-2)/a**3
   expected=np.array([x/a**2*math.exp(-y*y),b*math.sqrt(math.pi)*math.erf(y)/4]);phi=-x/a**2*math.sqrt(math.pi)*math.erf(y)/2;d=b*math.exp(-y*y)/2
   ck('manufactured V '+str((tag,x,y)),np.max(abs(z['V']-expected))<3e-13)
   ck('manufactured Phi/divergence '+str((tag,x,y)),abs(z['Phi']-phi)<3e-13 and abs(z['dV2_dy']-d)<3e-13)
 # Existing96 export validates this coordinate recipe at one known array.
 import torch
 from q_local_checkpoint import QLocalCheckpoint
 torch.set_num_threads(1)
 source='research/hydrostatic_function_space_audit/verification/hsG_c2.0_N96_log.pt';bind(source,'4ad484e6391001597ab57d501c8b3f644259af7b4c217b5032a28b00be609d01')
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(source)
 ep='research/hydrostatic_actual_node_export_audit/verification/source_nodes_maps.npz';bind(ep,'071b990c7a9ee3a91faeca5a1cc8c7d9ef6ef478f41ccd591fbe1ad5575d42d7')
 with np.load(ep,allow_pickle=False)as a:ex=np.column_stack([a['X'],a['Y']])
 ck('96 exact reconstruction',np.array_equal(coordinates(q),ex))
 inp=json.loads((V/'INPUTS.json').read_text())
 for a in inp['states']+[inp['full224']]:bind(a['path'],a['sha256'])
 models={}
 for a in inp['states']:
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(a['path'])
  models[q.N]=q;ck('actual input shape '+str(q.N),q.N==a['N']and q.M==a['M']and q.basis=='local'and q.cl==2 and q.kappa==2 and q.L==1 and len(q.u)==sum(q.N+1-k for k in range(q.M))and np.isfinite(q.u).all())
  ck('actual coordinate positivity '+str(q.N),np.isfinite(coordinates(q)).all()and(coordinates(q)>0).all())
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):qf=QLocalCheckpoint(inp['full224']['path'])
 ck('224 full raw numeric equivalence',np.array_equal(qf.u,models[224].u)and np.array_equal(qf.tk,models[224].tk)and all(getattr(qf,k)==getattr(models[224],k)for k in ['N','M','basis','L','cl','kappa','p']))
 # Snapshot failures use only synthetic rows and are stored in a dedicated manufacture directory.
 root=V/'store_manufactures';root.mkdir(exist_ok=True);xy=np.column_stack([np.arange(70)+1.,np.ones(70)]);jj=np.ones((70,4));ids=np.arange(70);b={'source':'synthetic'};rule=RULES['B'];path=root/'resume.npz'
 def compute(i):
  z={k:np.zeros(sh)for k,sh in SHAPES.items()};z['velocity']=np.array([float(i),1.]);z['residual']=rounded_fields(*xy[i],jj[i],z['velocity']);return z
 if path.exists():path.unlink()
 store=NodeStore(path,'test',ids,xy,jj,rule,b)
 class Stop(Exception):pass
 def stop(done,i):raise Stop()
 try:store.run(compute,stop)
 except Stop:pass
 ck('saved interruption64',store.done==64)
 store=NodeStore(path,'test',ids,xy,jj,rule,b);ck('resume prefix64',store.done==64);data=store.run(compute);ck('resume completed70',store.done==70)
 def reject(name,fun):
  try:fun()
  except (ValueError,AssertionError):ck(name,True);return
  raise AssertionError('accepted '+name)
 reject('positive denominator underflow rejected',lambda:rounded_fields(.5,0,[0,np.nextafter(0.,1),0,0],[-.5,0],c=1))
 reject('changed binding rejected',lambda:NodeStore(path,'test',ids,xy,jj,rule,{'source':'changed'}))
 reject('changed static targets rejected',lambda:NodeStore(path,'test',ids,xy+1,jj,rule,b))
 store=NodeStore(path,'test',ids,xy,jj,rule,b)
 def changed(i):z=compute(i);z['velocity'][0]+=1;return z
 reject('boundary replay corruption',lambda:store.run(changed))
 with np.load(path,allow_pickle=False)as a:bad={k:a[k]for k in a.files}
 m=json.loads(str(bad['manifest']));m.update(completed=64,status='RUNNING');bad['manifest']=np.array(json.dumps(m));bp=root/'bad_suffix.npz';np.savez_compressed(bp,**bad)
 reject('invalid suffix rejected',lambda:NodeStore(bp,'test',ids,xy,jj,rule,b))
 bad['manifest']=np.array(json.dumps(dict(m,completed=70,status='COMPLETE')));bad['residual']=bad['residual'].copy();bad['residual'][0,3]=np.nan;bp=root/'bad_ratio.npz';np.savez_compressed(bp,**bad)
 reject('undefined positive denominator rejected',lambda:NodeStore(bp,'test',ids,xy,jj,rule,b))
 pp=pair_spreads([1.,2.],[4.,5.,-3.,0.],[[2.,7.],[2.,7.],[2.,7.]])
 ck('identical rule spread',pp['spread']=='0'and pp['empirical_pass']and len(pp['components'])==6)
 pp=pair_spreads([0.,0.],[0.,0.,0.,0.],[[0.,0.]]*3);ck('zero spread explicit undefined',pp['zero_B_R']and pp['zero_B_Nf']and pp['spread_over_B_Nf']is None and all(a['both_zero']for a in pp['components']))
 # Real-rule saved replay on independently known smooth manufactured data.
 realxy=np.array([[.25,.4],[1.,2.]]);realj=jet(realxy[:,0],realxy[:,1]);realpath=root/'real_rule_resume.npz'
 if realpath.exists():realpath.unlink()
 def realcompute(i):
  z=evaluate(jet,*realxy[i],.5,RULES['B']);return dict(velocity=z['V'],Phi=z['Phi'],dV2dy=z['dV2_dy'],tail_velocity=z['tail_V'],metadata=z['meta'],residual=rounded_fields(*realxy[i],realj[i],z['V']))
 realstore=NodeStore(realpath,'real',np.arange(2),realxy,realj,RULES['B'],b);realstore.run(realcompute)
 realstore=NodeStore(realpath,'real',np.arange(2),realxy,realj,RULES['B'],b);original={k:a.copy()for k,a in realstore.arr.items()};realstore.run(realcompute)
 ck('real rule complete replay',all(np.array_equal(original[k],realstore.arr[k],equal_nan=True)for k in SHAPES))
 def realchanged(i):z=realcompute(i);z['Phi']+=1;return z
 reject('real quadrature altered replay rejected',lambda:realstore.run(realchanged))
 # Separate x/y parity and source-convention evidence at each admitted state.
 from independent_hydrostatic import CartesianQJet
 from larger_node_stage import coordinate_diagnostics
 for N,q in models.items():
  points=coordinates(q);ix=np.array([0,len(points)//2,len(points)-1]);a=points[ix];cj=CartesianQJet(q);j0=cj.jet(a[:,0],a[:,1])
  ck('separate x reflection '+str(N),np.array_equal(cj.jet(-a[:,0],a[:,1]),j0*np.array([1,-1,1,1])))
  ck('separate y reflection '+str(N),np.array_equal(cj.jet(a[:,0],-a[:,1]),j0*np.array([-1,-1,1,-1])))
  gd=coordinate_diagnostics(q,points);ck('hypot region agreement '+str(N),gd['classification_disagreement_count']==0 and min(gd['minimum_nominal_distance'])>1e-12)
  textpath=V/('producer_hs_node_check_c2_N'+str(N)+'.txt');bind(textpath)
  ck('positive M count '+str(N),('rows: M collocation angles AT THE SAME NODES ('+str(q.N*q.M)+' points):')in textpath.read_text())
 ck('review y-parity counterexample',not np.array_equal(jet([0.],[0.]),jet([0.],[-0.])*np.array([-1,1,-1,-1])))
 ck('review h-radius counterexample',2**-10<.004)
 ss=selection(xy,jj,data,np.zeros(70));ck('selection includes deterministic witnesses',all(i in ss['indices']for i in [0,35,69]))
 out=dict(status='PASS_LARGER_NODE_MANUFACTURES',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,scope='Synthetic tests and frozen input admission; no192/224 candidate inverse run.')
 (V/'MANUFACTURES.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks),out['utc'])
except Exception:
 (V/'MANUFACTURE_FAILURE.json').write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,traceback=traceback.format_exc()),indent=2)+'\n');raise
