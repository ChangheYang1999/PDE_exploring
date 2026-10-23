"""Result320 sole-heavy worker. Static producer records are never imported."""
from pathlib import Path
from datetime import datetime,timezone
import os,sys,json,hashlib,time,traceback,resource,fcntl
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
if sys.flags.optimize:raise SystemExit('optimized Python prohibited')
sys.set_int_max_str_digits(1000000)
import numpy as np
import torch
import accurate_map_stage as stage
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
R=stage.R;V=stage.V;O=V/'candidate';O.mkdir(exist_ok=True)
now=stage.now;sha=stage.sha;put=stage.put;start=now();tick=time.monotonic();checks=[];bindings={};artifacts={}
def ck(name,b,evidence=None):
 checks.append(dict(name=name,passed=bool(b),evidence=evidence))
 if not b:raise AssertionError((name,evidence))
def bind(p,h=None):
 p=str(p);x=sha(p);ck('binding '+p,(h is None or h==x)and(p not in bindings or bindings[p]==x));bindings[p]=x;return Path(p)
def load(p):
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):return QLocalCheckpoint(p)
def gate(p,status):
 d=json.loads(bind(p).read_text());ck('gate '+str(p),d['status']==status and all(z['passed']for z in d['checks'])and d['count']==len(d['checks']))
 for p,h in d.get('bindings',{}).items():bind(p,h)
 return d
try:
 lock=(V/'worker.lock').open('a');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
 ck('nice19',os.getpriority(os.PRIO_PROCESS,0)>=19);resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3));torch.set_num_threads(1)
 for name in ['JOB.json','MP_JOB.json']:
  p=Path('research/hydrostatic_larger_node_audit/verification')/name;d=json.loads(bind(p).read_text());proc=Path('/proc')/str(d['pid'])
  if proc.exists():
   stat=(proc/'stat').read_text().rsplit(') ',1)[1].split()[0];cmd=(proc/'cmdline').read_bytes();ck('318 ceased '+name,stat=='Z'or not any(s in cmd for s in [b'run_larger_node_audit.py',b'launch_larger_node_mp.py',b'run_larger_node_mp.py']))
 for folder,status in [('candidate','COMPLETE_FINITE_LARGER_NODES_REQUIRES_MP_AND_FINAL_REVIEW'),('mp','COMPLETE_LARGER_NODE_MP_REQUIRES_INDEPENDENT_FINAL_AUDIT')]:
  p=Path('research/hydrostatic_larger_node_audit/verification')/folder/'COMPLETE.json';d=json.loads(bind(p).read_text());ck('318 completed '+folder,d['status']==status and d['count']==len(d['checks'])and all(z['passed']for z in d['checks']))
 accept=json.loads(bind(V/'DESIGN_ACCEPTANCE.json').read_text());ck('accepted design',accept['status']=='ACCEPTED_FOR_FINITE_AUXILIARY_COMPUTATION')
 for p,h in accept['bindings'].items():bind(p,h)
 gate(V/'MANUFACTURES.json','PASS_ACCURATE_MAP_MANUFACTURES')
 gate(V/'RECORD_CHECKS.json','PASS_FROZEN_ACCURATE_MAP_RECORD_CONSISTENCY')
 sources={}
 for name in ['INPUTS.json','INPUTS_SUPPLEMENT.json','INPUTS_ADDITIONAL.json']:
  d=json.loads(bind(V/name).read_text())
  for z in d['files']:bind(z['frozen'],z['sha256']);sources[Path(z['frozen']).name]=z['frozen']
 for mod in [stage,sys.modules['independent_hydrostatic'],sys.modules['q_local_checkpoint'],sys.modules['q_checkpoint_reader'],sys.modules['node_export_inverse_stage'],sys.modules['larger_node_stage'],sys.modules['larger_node_independent_arithmetic']]:ck('own module '+mod.__name__,Path(mod.__file__).resolve().parent==Path('independent_code').resolve());bind(mod.__file__)
 for p in [__file__]+[R/name for name in ['PROOF.md','EXECUTION_PROOF.md','IMPORT_AND_CACHE_CORRECTION_PROOF.md','NONCONSTANT_MANUFACTURE_PROOF.md','RECORD_AUDIT_PROOF.md','RECORD_SCHEMA_CORRECTION_PROOF.md','DESIGN_REVIEW_RESOLUTION_PROOF.md']]:bind(p)
 base=dict(bindings);summary=[];models={};xy=stage.probe_grid();ck('finite probe grid',np.isfinite(xy).all()and xy.shape[1]==2 and len(xy)>700)
 state_paths={tag:sources[name]for tag,name in stage.STATES};state_paths.update(S96=sources['standard96.pt'],S128=sources['standard128c.pt'],S160=sources['hsG_c2.0_N160_log.pt'])
 # Keep only tiny coefficient readers; no complete polynomial tables are retained.
 for tag,path in state_paths.items():
  q=load(path);ck('parameters '+tag,q.cl==2 and q.kappa==2 and q.L==1 and q.p==.5 and q.basis=='local'and q.meta['basis_nodes_source']=='stored'and np.isfinite(q.u).all());ck('declared dimensions '+tag,(q.N,q.M)=={'A':(96,24),'B':(128,32),'C':(96,24),'E':(96,24),'G80':(80,20),'G96':(96,24),'G112':(112,28),'G128':(128,32),'S96':(96,24),'S128':(128,32),'S160':(160,40)}[tag]);models[tag]=q
 for tag,_ in stage.STATES:
  q=models[tag];jet=CartesianQJet(q).jet;N=q.N;target=O/(tag+'_targets.npz');jj=jet(xy[:,0],xy[:,1]);ck('finite jets '+tag,jj.shape==(len(xy),4)and np.isfinite(jj).all())
  if target.exists():
   old=stage.read_array(target);ck('unchanged targets '+tag,set(old)=={'xy','jets'}and np.array_equal(old['xy'],xy)and np.array_equal(old['jets'],jj))
  else:stage.save_array(target,dict(xy=xy,jets=jj))
  bb=dict(base);bb[str(target)]=sha(target);B=stage.phase(O/(tag+'_B.npz'),tag,'B',np.arange(len(xy)),xy,jj,jet,.5,bb)
  selection=stage.select(xy,jj,B);sp=O/(tag+'_SELECTION.json')
  if sp.exists():ck('unchanged selector '+tag,json.loads(sp.read_text())==selection)
  else:put(sp,selection)
  ab=dict(bb);ab[str(sp)]=sha(sp);ids=selection['indices'];A=stage.phase(O/(tag+'_A.npz'),tag,'A',ids,xy,jj,jet,.5,ab);C=stage.phase(O/(tag+'_C.npz'),tag,'C',ids,xy,jj,jet,.5,ab)
  comparisons=[]
  for k,i in enumerate(ids):
   rec=stage.pair_spreads(xy[i],jj[i],[A['velocity'][k],B['velocity'][i],C['velocity'][k]]);rec.update(index=i,x=float(xy[i,0]),y=float(xy[i,1]));comparisons.append(rec)
  counts={label:stage.audit_rows(xy,jj,z,ids0)for label,z,ids0 in [('B',B,range(len(xy))),('A',A,ids),('C',C,ids)]};ck('all independent arithmetic '+tag,counts==dict(B=5*len(xy),A=5*len(ids),C=5*len(ids)),counts)
  center_path=O/(tag+'_CENTER.json')
  if center_path.exists():center=json.loads(center_path.read_text());ck('cached exact center source '+tag,center['source_sha256']==sha(q.path) and center['bindings']==bb)
  else:center=stage.exact_center(q);center['bindings']=bb;put(center_path,center)
  mp_path=O/(tag+'_LOCAL_MP.json')
  if mp_path.exists():mp_data=json.loads(mp_path.read_text());ck('cached MP binding '+tag,mp_data['bindings']==bb and [z['index']for z in mp_data['results']]==ids)
  else:mp_data=dict(bindings=bb,results=stage.local_mp(q,xy,jj,ids),scope='Independent scalar reconstruction/differentiation at72/108 decimal digits, sharing the checkpoint coefficient split and stored nodes. Sensitivity, not a certified error.');put(mp_path,mp_data)
  mirrors=jet(-xy[ids,0],xy[ids,1]);ck('x parity '+tag,np.array_equal(mirrors,jj[ids]*[1,-1,1,1]));ck('y parity '+tag,np.array_equal(jet(xy[ids,0],-xy[ids,1]),jj[ids]*[-1,-1,1,-1]))
  record=dict(tag=tag,N=N,M=q.M,source_path=str(q.path),source_sha256=sha(q.path),points=len(xy),regions=stage.regional(xy,B['residual']),extents={str(e):stage.regional(xy,B['residual'],e)for e in stage.EXTENTS},selected=selection,comparisons=comparisons,center= center['rounded'],mp_precision_all_pass=all(d['precision_pass']for z in mp_data['results']for d in z['diagnostics']),arithmetic_counts=counts,mp_precision_failures=[dict(index=z['index'],component=k,diagnostic=d)for z in mp_data['results']for k,d in enumerate(z['diagnostics'])if not d['precision_pass']],extent_rounding=stage.extent_rounding(xy,stage.probe_nominal_radius()),center_inverse=stage.center_inverse_diagnostics(xy,B,center))
  put(O/(tag+'_COMPLETE.json'),record);summary.append(record)
  for p in [target,sp,center_path,mp_path,O/(tag+'_COMPLETE.json')]+[O/(tag+'_'+lab+'.npz')for lab in ['A','B','C']]:artifacts[str(p)]=sha(p)
  print('STATE COMPLETE',tag,now(),flush=True)
 # A separate direct angular experiment, with no interpolation substituted for its collocation evaluations.
 rings=[]
 for tag in ['B','G128']:
  q=models[tag];jet=CartesianQJet(q).jet;ax,dense,coll,blocks=stage.angular_grid(q.M);aj=jet(ax[:,0],ax[:,1]);tp=O/(tag+'_angular_targets.npz')
  if tp.exists():d=stage.read_array(tp);ck('same angular grid '+tag,np.array_equal(d['xy'],ax)and np.array_equal(d['jets'],aj))
  else:stage.save_array(tp,dict(xy=ax,jets=aj,dense=dense,collocation=coll))
  bb=dict(base);bb[str(tp)]=sha(tp);B=stage.phase(O/(tag+'_angular_B.npz'),tag+'_angular','B',np.arange(len(ax)),ax,aj,jet,.5,bb);ck('angular independent arithmetic '+tag,stage.audit_rows(ax,aj,B,range(len(ax)))==5*len(ax))
  out=stage.angular_summary(dense,coll,blocks,B['residual'],q.M);ids=sorted({z[k]for z in out for k in ['dense_argmax','collocation_argmax']});comparisons=[]
  asp=O/(tag+'_angular_SELECTION.json');aselect=dict(indices=ids,reason='dense and direct collocation Rf maxima on each of four rings')
  if asp.exists():ck('same angular selection '+tag,json.loads(asp.read_text())==aselect)
  else:put(asp,aselect)
  ab=dict(bb);ab[str(asp)]=sha(asp)
  A=stage.phase(O/(tag+'_angular_A.npz'),tag+'_angular','A',ids,ax,aj,jet,.5,ab);C=stage.phase(O/(tag+'_angular_C.npz'),tag+'_angular','C',ids,ax,aj,jet,.5,ab)
  for label,z in [('A',A),('C',C)]:ck('angular independent arithmetic '+tag+label,stage.audit_rows(ax,aj,z,ids)==5*len(ids))
  for k,i in enumerate(ids):d=stage.pair_spreads(ax[i],aj[i],[A['velocity'][k],B['velocity'][i],C['velocity'][k]]);d['index']=i;comparisons.append(d)
  record=dict(tag=tag,rows=len(ax),summary=out,comparisons=comparisons);put(O/(tag+'_ANGULAR.json'),record);rings.append(record)
  for p in [tp,asp,O/(tag+'_ANGULAR.json')]+[O/(tag+'_angular_'+lab+'.npz')for lab in ['A','B','C']]:artifacts[str(p)]=sha(p)
 pairs=[('G80','G96'),('G96','G112'),('G112','G128'),('E','G96'),('S96','A'),('S128','B'),('S96','C'),('S96','E'),('E','G128'),('S128','G128'),('G128','S160')];functions=[]
 for shift in [False,True]:
  name='shifted'if shift else'common';fx,rr=stage.common_grid(shift);fp=O/(name+'_fields.npz');vals={tag:CartesianQJet(q).jet(fx[:,0],fx[:,1])[:,:3]for tag,q in models.items()};ck('finite common jets '+name,all(np.isfinite(v).all()for v in vals.values()))
  fields=dict(xy=fx,nominal_radius=rr,**vals)
  if fp.exists():d=stage.read_array(fp);ck('same common fields '+name,set(d)==set(fields)and all(np.array_equal(v,d[k])for k,v in fields.items()))
  else:stage.save_array(fp,fields)
  records=[dict(pair=[a,b],legacy_denominator_state=b,orientation_scope='Verifier-chosen ordered pair; producer comparison orientation is not asserted here.',regions=stage.function_difference(vals[a],vals[b],rr))for a,b in pairs];rec=dict(grid=name,points=len(fx),records=records,radius_scope='nominal grid radius, half-open masks; final radius1e7 excluded from far_high');put(O/(name+'_COMPARISONS.json'),rec);functions.append(rec);artifacts[str(fp)]=sha(fp);artifacts[str(O/(name+'_COMPARISONS.json'))]=sha(O/(name+'_COMPARISONS.json'))
 for p,h in base.items():ck('stable '+p,sha(p)==h)
 out=dict(status='COMPLETE_FINITE_ACCURATE_MAP_REQUIRES_FINAL_AUDIT',started_utc=start,finished_utc=now(),elapsed_seconds=time.monotonic()-tick,count=len(checks),checks=checks,bindings=base,artifacts=artifacts,states=summary,angular=rings,function_comparisons=functions,versions=dict(numpy=np.__version__,torch=torch.__version__,python=sys.version),scope='Independent finite auxiliary hydrostatic trial diagnostics. No certified quadrature error, continuum convergence, historical execution authentication, or primary IPM endpoint.')
 put(O/'COMPLETE.json',out);print(out['status'],now(),flush=True)
except Exception:
 put(O/('FAILURE_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'.json'),dict(utc=now(),checks=checks,bindings=bindings,traceback=traceback.format_exc()));raise
