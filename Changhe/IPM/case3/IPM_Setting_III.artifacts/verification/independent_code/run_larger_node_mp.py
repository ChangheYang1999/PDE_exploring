"""Selected finite MP audit of frozen larger-grid nodes; sole-heavy process."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import os,json,hashlib,time,traceback,sys,resource
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
R=Path('research/hydrostatic_larger_node_audit');V=R/'verification';fixture=len(sys.argv)>1
if fixture:
 assert len(sys.argv)==3 and sys.argv[1]=='--fixture'
 target=Path(sys.argv[2]);target.resolve().relative_to((V/'mp_driver_manufactures').resolve());V=target
C=V/'candidate';O=V/'mp';O.mkdir(exist_ok=True)
if (O/'COMPLETE.json').exists():raise FileExistsError('completed output preserved; no rerun')
if (O/'FAILURE.json').exists():(O/'FAILURE.json').rename(O/('FAILURE_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json'))
now=lambda:datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();start=now();tick=time.perf_counter();checks=[];bindings={};aliases={}
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e));assert b,(n,e)
def bind(p,h=None):
 p=str(p);hh=sha(p);alias=str(Path(p).resolve());ck('binding '+p,(h is None or h==hh)and(p not in bindings or bindings[p]==hh)and(alias not in aliases or aliases[alias]==hh));bindings[p]=hh;aliases[alias]=hh;return Path(p)
def save(p,d):
 t=p.with_suffix('.tmp');t.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n');t.replace(p)
try:
 for p in [__file__,R/'MP_EXECUTION_PROOF.md',R/'MP_MANUFACTURE_AND_GATE_PROOF.md',R/'MP_REVIEW_RESOLUTION_PROOF.md',R/'MP_ADMISSION_REPLAY_PROOF.md','independent_code/launch_larger_node_mp.py','independent_code/node_export_mp_chunks.py','independent_code/node_export_mp_integrand.py','independent_code/scalar_mp_hydrostatic_density.py','independent_code/larger_node_stage.py','independent_code/node_export_inverse_stage.py','independent_code/independent_hydrostatic.py','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py']:bind(p)
 ap=Path(os.environ['IPM318_MP_ADMISSION']);ah=sha(ap);admission=json.loads(ap.read_text());policy=json.loads(bind(V/'MP_PROCESS_POLICY.json',admission['policy_sha256']).read_text());ck('stable process policy',policy['schema']=='IPM318_MP_POLICY_V1'and policy['synthetic_only']==fixture and policy['wrapper_sha256']==sha('independent_code/launch_larger_node_mp.py')and policy['driver_sha256']==sha(__file__)and policy['nice']==19 and policy['memory_limit_bytes']==14*1024**3 and policy['timeout_seconds']==(180 if fixture else 14400));ck('wrapper process admission',admission['schema']=='IPM318_MP_ADMISSION_V1'and admission['synthetic_only']==fixture and admission['wrapper_sha256']==sha('independent_code/launch_larger_node_mp.py')and admission['driver_sha256']==sha(__file__)and admission['lock_held']and os.getpriority(os.PRIO_PROCESS,0)==19 and resource.getrlimit(resource.RLIMIT_AS)==(14*1024**3,14*1024**3))
 a=json.loads(bind(V/'MP_DESIGN_ACCEPTANCE.json').read_text());ck('actual MP design accepted',a['status']==('SYNTHETIC_TEST_ONLY'if fixture else'ACCEPTED_FOR_FINITE_MP_COMPUTATION'))
 for p,h in a['bindings'].items():bind(p,h)
 manuf=json.loads(bind(V/'MP_STAGE_MANUFACTURES.json').read_text());ck('MP manufactures semantic gate',manuf['status']=='PASS_MP_GEOMETRY_MOMENTS_AND_REAL_RESTART'and manuf['count']==len(manuf['checks'])and all(z['passed']for z in manuf['checks']))
 for p,h in manuf['bindings'].items():bind(p,h)
 inputs=json.loads(bind(V/'INPUTS.json').read_text());expectedstates=inputs['states'];ck('exact state order',[(s['N'],s['M'])for s in expectedstates]==([(2,1)]if fixture else[(224,56),(192,48)]))
 for ss in expectedstates:bind(ss['path'],ss['sha256'])
 c=json.loads(bind(C/'COMPLETE.json').read_text());ck('finite all-node stage complete',c['status']=='COMPLETE_FINITE_LARGER_NODES_REQUIRES_MP_AND_FINAL_REVIEW'and c['count']==len(c['checks'])and all(z['passed']for z in c['checks']))
 for p,h in {**c['bindings'],**c['artifacts']}.items():bind(p,h)
 import numpy as np
 import torch
 import mpmath as mp
 versions=dict(python=sys.version,numpy=np.__version__,torch=torch.__version__,mpmath=mp.__version__,numeric_pickle='weights_only=True; ndarray,_reconstruct plus scalar,dtype,float64/float32 dtype constructors')
 from q_local_checkpoint import QLocalCheckpoint
 from independent_hydrostatic import CartesianQJet
 from scalar_mp_hydrostatic_density import ScalarMPDensity
 from node_export_mp_chunks import MPChunkStore,decimal_value
 from node_export_mp_integrand import frozen_geometry,exact_moments,exact_components,compare_decimal_rows,COMPONENT_NAMES
 from node_export_inverse_stage import RULES
 from larger_node_stage import exact_fields,rounded_fields,coordinates
 for name in ['q_local_checkpoint','q_checkpoint_reader','independent_hydrostatic','scalar_mp_hydrostatic_density','node_export_mp_chunks','node_export_mp_integrand','node_export_inverse_stage','larger_node_stage']:
  import sys
  ck('own module path '+name,Path(sys.modules[name].__file__).resolve().parent==Path('independent_code').resolve())
 torch.set_num_threads(1)
 def load(p):
  with np.load(p,allow_pickle=False)as z:return {k:z[k]for k in z.files}
 def artifact(p):
  ck('explicit loaded artifact '+str(p),str(p)in c['artifacts']);return bind(p,c['artifacts'][str(p)])
 def bothzeros(high,double):return [sum(decimal_value(row[k])==0 and F(float(dd[k]))==0 for row,dd in zip(high,double))for k in range(len(high[0]))]
 def ledger(geom,rows,y):
  pp={k:F(0)for k in ['Jx','Jxx','Ix_outer','Ixx_outer','Ix_tail','Ixx_tail']};nn=dict(pp);names=list(pp)
  for i in range(len(geom['node'])):
   ph=int(geom['phase'][i]);w=F(float(geom['weight'][i]))*(F(float(geom['node'][i]))if ph==0 else 1);ds=[F(float(z))for z in geom['derivatives'][i]]if rows is None else[decimal_value(z)for z in rows[i]]
   for k in range(2):
    z=w*ds[k];name=names[2*ph+k]
    if z>=0:pp[name]+=z
    else:nn[name]+=z
  def entry(p,n):return dict(positive=str(p),negative=str(n),total=str(p+n),sum_absolute=str(p-n),cancellation_ratio=str((p-n)/abs(p+n))if p+n else None)
  cc={};terms=[[(2,-1),(4,-1)],[(1,1),(3,y),(5,y)],[(0,1),(2,y),(4,y)],[(3,1),(5,1)],[(4,-1)],[(5,y)]]
  for name,ts in zip(COMPONENT_NAMES,terms):
   p=n=F(0)
   for index,factor in ts:
    key=names[index]
    if factor>=0:p+=factor*pp[key];n+=factor*nn[key]
    else:p+=factor*nn[key];n+=factor*pp[key]
   cc[name]=entry(p,n)
  return dict(moments={k:entry(pp[k],nn[k])for k in names},components=cc)
 ck('completed states equal frozen order',[ss['source']for ss in c['results']]==expectedstates)
 base=dict(bindings);results=[]
 for state in c['results']:
  N=state['N'];tag='N'+str(N);d=load(artifact(C/(tag+'_targets.npz')));B=load(artifact(C/(tag+'_B.npz')));CC=load(artifact(C/(tag+'_C.npz')));selection=json.loads(artifact(C/(tag+'_SELECTION.json')).read_text());statefile=json.loads(artifact(C/(tag+'_COMPLETE.json')).read_text());ck('per-state complete identity '+tag,statefile==state);xy,jets=d['xy'],d['jets'];ids=state['local_mp_indices'];witnesses=state['integrand_mp_indices']
  ck('selected indices '+tag,ids==state['selected']['indices']==sorted(set(ids))and set(witnesses)<=set(ids)and all(type(i)is int and 0<=i<len(xy)for i in ids))
  cm=json.loads(str(CC['manifest']));ck('actual completed C selection '+tag,cm['status']=='COMPLETE'and cm['completed']==cm['total']==len(ids)and np.array_equal(CC['indices'],ids)and selection==state['selected']and selection['indices']==ids)
  finite=np.flatnonzero(np.isfinite(B['residual'][:,3]));ck('unique declared global Rf witness '+tag,len(witnesses)==1 and len(finite)>0 and witnesses[0]==int(finite[np.argmax(B['residual'][finite,3])]))
  undefined=int(len(xy)-len(finite))
  m=json.loads(str(B['manifest']));ck('B complete shape/order/rule '+tag,m['status']=='COMPLETE'and m['completed']==m['total']==N*state['M']and m['rule']==RULES['B']and np.array_equal(B['indices'],np.arange(len(xy)))and np.array_equal(B['xy'],xy)and np.array_equal(B['jets'],jets))
  for i in range(len(xy)):
   if not np.array_equal(B['residual'][i],rounded_fields(*xy[i],jets[i],B['velocity'][i]),equal_nan=True):raise ArithmeticError('stored B operands '+str((N,i)))
  ck('all B finite arithmetic verified '+tag,True,len(xy))
  bind(state['source']['path'],state['source']['sha256'])
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(state['source']['path'])
  ck('same exact state '+tag,q.N==N and q.M==state['M']and q.cl==2 and q.kappa==2 and q.L==1 and q.p==.5 and q.basis=='local'and q.meta['basis_nodes_source']=='stored'and q.meta['sha256']==state['source']['sha256']and np.array_equal(coordinates(q),xy))
  local={};lb=dict(base,selected_indices=json.dumps(ids),state_N=str(N))
  for digits in [72,108]:
   with mp.workdps(digits):model=ScalarMPDensity(q.coeff,q.L,q.kappa,q.basis,q.tk)
   local[digits]=MPChunkStore(O/(tag+'_local_'+str(digits)),len(ids),digits,4,lb).run(lambda k:model.jet(*map(float,xy[ids[k]])),lambda n:print('LOCAL',N,digits,n,'/',len(ids),now(),flush=True))
  comparison=compare_decimal_rows(local[72],local[108],jets[ids],'1e-60','1e-50')
  local_locations={key:[dict(z,original_index=ids[z['index']],x=float(xy[ids[z['index']],0]),y=float(xy[ids[z['index']],1]))for z in comparison[key]]for key in ['precision_maxima','double_pure_relative_maxima']}
  localout=dict(N=N,locations=local_locations,both_zero_counts=bothzeros(local[108],jets[ids]),indices=ids,rows72=local[72],rows108=local[108],comparison=comparison,chunk_bindings=lb,scope='Selected scalar MP local jets, finite sensitivity only')
  save(O/(tag+'_LOCAL_COMPLETE.json'),localout);stateout=dict(N=N,M=q.M,local=localout,witnesses=[],B_Rf_undefined_count=undefined);jet=CartesianQJet(q).jet
  for index in witnesses:
   xx,yy=map(float,xy[index]);ck('positive target '+str((N,index)),xx>0 and yy>0);geom=frozen_geometry(jet,xx,yy,q.p,RULES['B']);ref=np.r_[B['velocity'][index],B['Phi'][index],B['dV2dy'][index],B['tail_velocity'][index]]
   ck('bitwise B geometry replay '+str((N,index)),geom['reference'].tobytes()==ref.tobytes()and geom['metadata'].tobytes()==B['metadata'][index].tobytes())
   ck('finite positive geometry '+str((N,index)),all(np.isfinite(a).all()for a in geom.values())and (geom['node']>0).all()and (geom['weight']>0).all())
   gp=O/(tag+'_geometry_'+str(index)+'.npz');arrays=dict(geom,manifest=np.array(json.dumps(dict(N=N,index=index,bindings=base,rule=RULES['B']),sort_keys=True)))
   if gp.exists():
    old=load(gp);ck('identical existing geometry '+str((N,index)),set(old)==set(arrays)and all(old[k].dtype==arrays[k].dtype and old[k].shape==arrays[k].shape and old[k].tobytes()==arrays[k].tobytes()for k in arrays))
   else:
    tmp=gp.with_suffix('.tmp')
    with tmp.open('wb')as h:np.savez_compressed(h,**arrays)
    tmp.replace(gp)
   gb=dict(base);gb[str(gp)]=sha(gp);rows={};nodes=geom['node']
   for digits in [72,108]:
    with mp.workdps(digits):model=ScalarMPDensity(q.coeff,q.L,q.kappa,q.basis,q.tk)
    def integrand(k):
     x=mp.mpf(xx);y=mp.mpf(float(nodes[k]));return [mp.diff(lambda z:model.density(z,y),x,addprec=40),mp.diff(lambda z:model.density(z,y),x,2,addprec=40)]
    rows[digits]=MPChunkStore(O/(tag+'_integrand_'+str(index)+'_'+str(digits)),len(nodes),digits,2,gb).run(integrand,lambda n:print('INTEGRAND',N,index,digits,n,'/',len(nodes),now(),flush=True))
   diag=compare_decimal_rows(rows[72],rows[108],geom['derivatives'],'1e-80','1e-50')
   for key in ['precision_maxima','double_pure_relative_maxima']:
    for z in diag[key]:z.update(phase=int(geom['phase'][z['index']]),physical_y=float(nodes[z['index']]))
   failed_locations=[dict(node=int(z[0]),component=int(z[1]),scaled=z[2],phase=int(geom['phase'][int(z[0])]),physical_y=float(nodes[int(z[0])]),target=index)for z in diag['precision_failed_entries']]
   moments={label:exact_moments(geom,rr)for label,rr in [('D',None),('M72',rows[72]),('M108',rows[108])]};comps={label:exact_components(m,xx,yy)for label,m in moments.items()};bref=dict(zip(COMPONENT_NAMES,map(F,map(float,ref))));parts=[]
   for k in COMPONENT_NAMES:
    total=comps['M108'][k]-bref[k];dj=comps['M108'][k]-comps['D'][k];da=comps['D'][k]-bref[k];ck('component identity '+str((N,index,k)),total==dj+da)
    parts.append(dict(component=k,B=str(bref[k]),D=str(comps['D'][k]),M72=str(comps['M72'][k]),M108=str(comps['M108'][k]),total=str(total),integrand=str(dj),finite_arithmetic=str(da),precision_change=str(comps['M108'][k]-comps['M72'][k])))
   ledgers={label:ledger(geom,rr,F(yy))for label,rr in [('D',None),('M72',rows[72]),('M108',rows[108])]}
   for label in ledgers:
    ck('signed ledgers component totals '+str((N,index,label)),all(F(ledgers[label]['components'][k]['total'])==comps[label][k]for k in COMPONENT_NAMES))
   gradient=list(map(F,map(float,jets[index,1:3])));velocitykeys=['V1','V2'];total=sum((comps['M108'][k]-bref[k])*g for k,g in zip(velocitykeys,gradient));dj=sum((comps['M108'][k]-comps['D'][k])*g for k,g in zip(velocitykeys,gradient));da=sum((comps['D'][k]-bref[k])*g for k,g in zip(velocitykeys,gradient));ck('residual identity '+str((N,index)),total==dj+da)
   nf=F(float(B['residual'][index,1]));ck('positive stored Nf '+str((N,index)),nf>0)
   # At a common target, independently spell out all four jet/velocity combinations.
   mpj=list(map(decimal_value,local[108][ids.index(index)]));binj=list(map(F,map(float,jets[index])));x,y=F(xx),F(yy)
   def Rval(j,v):return (2*x+v[0])*j[1]+(2*y+v[1])*j[2]-j[0]
   bv=[bref[k]for k in velocitykeys];mv=[comps['M108'][k]for k in velocitykeys];rr00=Rval(binj,bv);rr10=Rval(mpj,bv);rr01=Rval(binj,mv);rr11=Rval(mpj,mv);cross=sum((mpj[k+1]-binj[k+1])*(mv[k]-bv[k])for k in range(2))
   ck('four-combination exact cross identity '+str((N,index)),rr11-rr00==(rr10-rr00)+(rr01-rr00)+cross and rr01-rr00==total)
   row=dict(N=N,index=index,x=xx,y=yy,nodes=len(nodes),geometry=str(gp),geometry_bindings=gb,integrand=diag,both_zero_counts=bothzeros(rows[108],geom['derivatives']),failed_locations=failed_locations,ledgers=ledgers,moments={label:{k:str(a)for k,a in m.items()}for label,m in moments.items()},components=parts,residual_change=dict(total=str(total),integrand=str(dj),finite_arithmetic=str(da),stored_B_Nf=str(nf),total_over_stored_B_Nf=str(total/nf)),four_combinations={k:str(a)for k,a in dict(R00=rr00,R10=rr10,R01=rr01,R11=rr11,cross=cross).items()},scope='Finite selected binary64 geometry and serialized MP operands, not continuum or quadrature certification')
   save(O/(tag+'_witness_'+str(index)+'.json'),row);stateout['witnesses'].append(row)
  results.append(stateout)
 for p,h in base.items():ck('stable '+p,sha(p)==h)
 ck('stable execution admission',sha(ap)==ah)
 artifacts={str(p):sha(p)for p in O.rglob('*')if p.is_file()and p.name not in ['COMPLETE.json','FAILURE.json']and not p.name.endswith('.tmp')}
 out=dict(status='COMPLETE_LARGER_NODE_MP_REQUIRES_INDEPENDENT_FINAL_AUDIT',synthetic_only=fixture,versions=versions,execution_admission=dict(path=str(ap),sha256=ah,record=admission),started_utc=start,finished_utc=now(),elapsed_seconds=time.perf_counter()-tick,count=len(checks),checks=checks,bindings=base,artifacts=artifacts,results=results,precision_diagnostics_passed=all(s['local']['comparison']['precision_diagnostic_passed']and all(w['integrand']['precision_diagnostic_passed']for w in s['witnesses'])for s in results),scope='Selected finite MP checks only; exact integral error OPEN; full-plane IPM UNRESOLVED.')
 save(O/'COMPLETE.json',out);print(out['status'],now(),flush=True)
except Exception:
 save(O/'FAILURE.json',dict(utc=now(),started_utc=start,count=len(checks),checks=checks,bindings=bindings,traceback=traceback.format_exc()));raise
