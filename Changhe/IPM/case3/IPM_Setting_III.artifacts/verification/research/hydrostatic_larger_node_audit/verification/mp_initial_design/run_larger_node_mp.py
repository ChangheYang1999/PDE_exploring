"""Selected finite MP audit of frozen larger-grid nodes; sole-heavy process."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import os,json,hashlib,time,traceback
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
R=Path('research/hydrostatic_larger_node_audit');V=R/'verification';C=V/'candidate';O=V/'mp';O.mkdir(exist_ok=True)
now=lambda:datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();start=now();tick=time.perf_counter();checks=[];bindings={}
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e));assert b,(n,e)
def bind(p,h=None):
 p=str(p);hh=sha(p);ck('binding '+p,(h is None or h==hh)and(p not in bindings or bindings[p]==hh));bindings[p]=hh;return Path(p)
def save(p,d):
 t=p.with_suffix('.tmp');t.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n');t.replace(p)
try:
 for p in [__file__,R/'MP_EXECUTION_PROOF.md',R/'MP_MANUFACTURE_AND_GATE_PROOF.md','independent_code/node_export_mp_chunks.py','independent_code/node_export_mp_integrand.py','independent_code/scalar_mp_hydrostatic_density.py','independent_code/larger_node_stage.py','independent_code/node_export_inverse_stage.py','independent_code/independent_hydrostatic.py','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py']:bind(p)
 a=json.loads(bind(V/'MP_DESIGN_ACCEPTANCE.json').read_text());ck('actual MP design accepted',a['status']=='ACCEPTED_FOR_FINITE_MP_COMPUTATION')
 for p,h in a['bindings'].items():bind(p,h)
 manuf=json.loads(bind(V/'MP_STAGE_MANUFACTURES.json').read_text());ck('MP manufactures semantic gate',manuf['status']=='PASS_MP_GEOMETRY_MOMENTS_AND_REAL_RESTART'and manuf['count']==len(manuf['checks'])and all(z['passed']for z in manuf['checks']))
 for p,h in manuf['bindings'].items():bind(p,h)
 c=json.loads(bind(C/'COMPLETE.json').read_text());ck('finite all-node stage complete',c['status']=='COMPLETE_FINITE_LARGER_NODES_REQUIRES_MP_AND_FINAL_REVIEW'and c['count']==len(c['checks'])and all(z['passed']for z in c['checks']))
 for p,h in {**c['bindings'],**c['artifacts']}.items():bind(p,h)
 import numpy as np
 import torch
 import mpmath as mp
 from q_local_checkpoint import QLocalCheckpoint
 from independent_hydrostatic import CartesianQJet
 from scalar_mp_hydrostatic_density import ScalarMPDensity
 from node_export_mp_chunks import MPChunkStore,decimal_value
 from node_export_mp_integrand import frozen_geometry,exact_moments,exact_components,compare_decimal_rows,COMPONENT_NAMES
 from node_export_inverse_stage import RULES
 from larger_node_stage import exact_fields,rounded_fields
 for name in ['q_local_checkpoint','q_checkpoint_reader','independent_hydrostatic','scalar_mp_hydrostatic_density','node_export_mp_chunks','node_export_mp_integrand','node_export_inverse_stage','larger_node_stage']:
  import sys
  ck('own module path '+name,Path(sys.modules[name].__file__).resolve().parent==Path('independent_code').resolve())
 torch.set_num_threads(1)
 def load(p):
  with np.load(p,allow_pickle=False)as z:return {k:z[k]for k in z.files}
 base=dict(bindings);results=[]
 for state in c['results']:
  N=state['N'];tag='N'+str(N);d=load(C/(tag+'_targets.npz'));B=load(C/(tag+'_B.npz'));xy,jets=d['xy'],d['jets'];ids=state['local_mp_indices'];witnesses=state['integrand_mp_indices']
  ck('selected indices '+tag,ids==state['selected']['indices']==sorted(set(ids))and set(witnesses)<=set(ids)and all(type(i)is int and 0<=i<len(xy)for i in ids))
  m=json.loads(str(B['manifest']));ck('B complete shape/order/rule '+tag,m['status']=='COMPLETE'and m['completed']==m['total']==N*state['M']and m['rule']==RULES['B']and np.array_equal(B['indices'],np.arange(len(xy)))and np.array_equal(B['xy'],xy)and np.array_equal(B['jets'],jets))
  for i in range(len(xy)):
   if not np.array_equal(B['residual'][i],rounded_fields(*xy[i],jets[i],B['velocity'][i]),equal_nan=True):raise ArithmeticError('stored B operands '+str((N,i)))
  ck('all B finite arithmetic verified '+tag,True,len(xy))
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(state['source']['path'])
  ck('same exact state '+tag,q.N==N and q.M==state['M']and q.cl==2 and q.kappa==2 and q.L==1 and q.p==.5)
  local={};lb=dict(base,selected_indices=json.dumps(ids),state_N=str(N))
  for digits in [72,108]:
   with mp.workdps(digits):model=ScalarMPDensity(q.coeff,q.L,q.kappa,q.basis,q.tk)
   local[digits]=MPChunkStore(O/(tag+'_local_'+str(digits)),len(ids),digits,4,lb).run(lambda k:model.jet(*map(float,xy[ids[k]])),lambda n:print('LOCAL',N,digits,n,'/',len(ids),now(),flush=True))
  comparison=compare_decimal_rows(local[72],local[108],jets[ids],'1e-60','1e-50')
  localout=dict(N=N,indices=ids,rows72=local[72],rows108=local[108],comparison=comparison,chunk_bindings=lb,scope='Selected scalar MP local jets, finite sensitivity only')
  save(O/(tag+'_LOCAL_COMPLETE.json'),localout);stateout=dict(N=N,M=q.M,local=localout,witnesses=[]);jet=CartesianQJet(q).jet
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
   moments={label:exact_moments(geom,rr)for label,rr in [('D',None),('M72',rows[72]),('M108',rows[108])]};comps={label:exact_components(m,xx,yy)for label,m in moments.items()};bref=dict(zip(COMPONENT_NAMES,map(F,map(float,ref))));parts=[]
   for k in COMPONENT_NAMES:
    total=comps['M108'][k]-bref[k];dj=comps['M108'][k]-comps['D'][k];da=comps['D'][k]-bref[k];ck('component identity '+str((N,index,k)),total==dj+da)
    parts.append(dict(component=k,B=str(bref[k]),D=str(comps['D'][k]),M72=str(comps['M72'][k]),M108=str(comps['M108'][k]),total=str(total),integrand=str(dj),finite_arithmetic=str(da),precision_change=str(comps['M108'][k]-comps['M72'][k])))
   gradient=list(map(F,map(float,jets[index,1:3])));velocitykeys=['V1','V2'];total=sum((comps['M108'][k]-bref[k])*g for k,g in zip(velocitykeys,gradient));dj=sum((comps['M108'][k]-comps['D'][k])*g for k,g in zip(velocitykeys,gradient));da=sum((comps['D'][k]-bref[k])*g for k,g in zip(velocitykeys,gradient));ck('residual identity '+str((N,index)),total==dj+da)
   nf=F(float(B['residual'][index,1]));ck('positive stored Nf '+str((N,index)),nf>0)
   # At a common target, independently spell out all four jet/velocity combinations.
   mpj=list(map(decimal_value,local[108][ids.index(index)]));binj=list(map(F,map(float,jets[index])));x,y=F(xx),F(yy)
   def Rval(j,v):return (2*x+v[0])*j[1]+(2*y+v[1])*j[2]-j[0]
   bv=[bref[k]for k in velocitykeys];mv=[comps['M108'][k]for k in velocitykeys];rr00=Rval(binj,bv);rr10=Rval(mpj,bv);rr01=Rval(binj,mv);rr11=Rval(mpj,mv);cross=sum((mpj[k+1]-binj[k+1])*(mv[k]-bv[k])for k in range(2))
   ck('four-combination exact cross identity '+str((N,index)),rr11-rr00==(rr10-rr00)+(rr01-rr00)+cross and rr01-rr00==total)
   row=dict(N=N,index=index,x=xx,y=yy,nodes=len(nodes),geometry=str(gp),geometry_bindings=gb,integrand=diag,moments={label:{k:str(a)for k,a in m.items()}for label,m in moments.items()},components=parts,residual_change=dict(total=str(total),integrand=str(dj),finite_arithmetic=str(da),stored_B_Nf=str(nf),total_over_stored_B_Nf=str(total/nf)),four_combinations={k:str(a)for k,a in dict(R00=rr00,R10=rr10,R01=rr01,R11=rr11,cross=cross).items()},scope='Finite selected binary64 geometry and serialized MP operands, not continuum or quadrature certification')
   save(O/(tag+'_witness_'+str(index)+'.json'),row);stateout['witnesses'].append(row)
  results.append(stateout)
 for p,h in base.items():ck('stable '+p,sha(p)==h)
 artifacts={str(p):sha(p)for p in O.rglob('*')if p.is_file()and p.name not in ['COMPLETE.json','FAILURE.json']and not p.name.endswith('.tmp')}
 out=dict(status='COMPLETE_LARGER_NODE_MP_REQUIRES_INDEPENDENT_FINAL_AUDIT',started_utc=start,finished_utc=now(),elapsed_seconds=time.perf_counter()-tick,count=len(checks),checks=checks,bindings=base,artifacts=artifacts,results=results,precision_diagnostics_passed=all(s['local']['comparison']['precision_diagnostic_passed']and all(w['integrand']['precision_diagnostic_passed']for w in s['witnesses'])for s in results),scope='Selected finite MP checks only; exact integral error OPEN; full-plane IPM UNRESOLVED.')
 save(O/'COMPLETE.json',out);print(out['status'],now(),flush=True)
except Exception:
 save(O/'FAILURE.json',dict(utc=now(),started_utc=start,count=len(checks),checks=checks,bindings=bindings,traceback=traceback.format_exc()));raise
