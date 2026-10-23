"""Single-process resumable local/finite-integrand MP sensitivity computation."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import os,json,hashlib,time,traceback
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';RULEDIR=V/'candidate_inverse';OUT=V/'candidate_mp_inverse';OUT.mkdir(exist_ok=True)
now=lambda:datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();start=now();tick=time.perf_counter();checks=[];bindings={}
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=str(Path(p).resolve().relative_to(Path.cwd()));z=sha(p);ck('binding '+p,(h is None or h==z)and(p not in bindings or bindings[p]==z));bindings[p]=z;return Path(p)
def save(p,d):
 p=Path(p);tmp=p.with_suffix(p.suffix+'.tmp');tmp.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n');tmp.replace(p)
def gate(name,status,count=None):
 p=bind(V/name);d=json.loads(p.read_text());ck('gate '+name,d['status']==status and d['count']==len(d['checks'])and all(z['passed']for z in d['checks'])and(count is None or d['count']==count))
 for p,h in d['bindings'].items():bind(p,h)
 return d
try:
 for p in [__file__,'independent_code/node_export_mp_chunks.py','independent_code/node_export_mp_integrand.py','independent_code/scalar_mp_hydrostatic_density.py','independent_code/node_export_inverse_stage.py','independent_code/independent_hydrostatic.py','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py',R/'MP_INTEGRAND_EXECUTION_PROOF.md',R/'MP_DESIGN_REVIEW_RESOLUTION_PROOF.md']:bind(p)
 old=gate('ACTUAL_MP_JETS.json','PASS_ACTUAL_LOCAL_MP_JET_WITNESSES',183)
 gate('MP_STAGE_MANUFACTURES.json','PASS_MP_GEOMETRY_MOMENTS_AND_REAL_RESTART')
 acceptance=json.loads(bind(V/'MP_DESIGN_ACCEPTANCE.json').read_text());ck('finite MP design accepted',acceptance['status']=='ACCEPTED_FOR_FINITE_MP_COMPUTATION')
 for p,h in acceptance['bindings'].items():bind(p,h)
 complete=json.loads(bind(RULEDIR/'RULES_COMPLETE.json').read_text());ck('A/B/C complete finite rules',complete['status']=='COMPLETE_FINITE_RULES_REQUIRES_LOCAL_MP_INTEGRAND_MP_AND_FINAL_REVIEW'and complete['count']==len(complete['checks'])and all(z['passed']for z in complete['checks']))
 for p,h in complete['bindings'].items():bind(p,h)
 for p,h in complete['artifacts'].items():bind(p,h)
 import numpy as np
 import torch
 import mpmath as mp
 from q_local_checkpoint import QLocalCheckpoint
 from independent_hydrostatic import CartesianQJet
 from scalar_mp_hydrostatic_density import ScalarMPDensity
 from node_export_mp_chunks import MPChunkStore,decimal_value
 from node_export_mp_integrand import frozen_geometry,exact_moments,exact_components,compare_decimal_rows,COMPONENT_NAMES
 from node_export_inverse_stage import RULES,RESIDUAL_COLUMNS,maxima
 torch.set_num_threads(1)
 def load(p):
  with np.load(p,allow_pickle=False)as f:return {k:f[k]for k in f.files}
 for name in ['B.npz','SELECTION.json']:
  p=RULEDIR/name;ck('explicit completed artifact '+name,str(p)in complete['artifacts']);bind(p,complete['artifacts'][str(p)])
 d=load(bind(V/'actual_node_jets.npz'));B=load(bind(RULEDIR/'B.npz'));selection=json.loads(bind(RULEDIR/'SELECTION.json').read_text());indices=selection['indices'];x,y=d['X'],d['Y'];own,prod=d['own_jet'],d['producer_jet']
 state=bind(json.loads((V/'PROVENANCE_INPUTS.json').read_text())['state']['frozen'],'4ad484e6391001597ab57d501c8b3f644259af7b4c217b5032a28b00be609d01')
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(state)
 ck('state parameters',q.N==96 and q.M==24 and q.L==1 and q.cl==2 and q.kappa==2 and q.p==.5 and q.basis=='local')
 ck('selection contains old MP witnesses',set(row['index']for row in old['rows'])<=set(indices))
 ck('selection sorted unique valid',indices==sorted(set(indices))and all(type(i)is int and 0<=i<2304 for i in indices))
 ck('B full node order',np.array_equal(B['indices'],np.arange(2304)))
 bmeta=json.loads(str(B['manifest']));ck('B named residual schema',bmeta['columns']['residual']==RESIDUAL_COLUMNS and RESIDUAL_COLUMNS==['R','Nf','Nv','Rf','Rv']);ck('B complete rule manifest',bmeta['phase']=='B'and bmeta['status']=='COMPLETE'and bmeta['completed']==bmeta['total']==2304 and bmeta['rule']==RULES['B'])
 nfrebuilt=[]
 for i in range(2304):
  g,gx,gy=map(F,map(float,own[i,:3]));vx,vy=map(F,map(float,B['velocity'][i]));xx,yy=map(F,map(float,[x[i],y[i]]));nf=abs((2*xx+vx)*gx)+abs((2*yy+vy)*gy)+abs(g);nfrebuilt.append(float(nf))
 ck('all B Nf exact operands round once',np.asarray(nfrebuilt,dtype=np.float64).tobytes()==np.ascontiguousarray(B['residual'][:,1]).tobytes())
 summary=maxima(x,y,B['residual']);witnesses=sorted({z['metrics']['absR']['index']for z in summary}|{1139})
 ck('declared MP integrand witnesses',witnesses==complete['mp_integrand_indices'])
 basebindings=dict(bindings);localrows={}
 for digits in [72,108]:
  with mp.workdps(digits):model=ScalarMPDensity(q.coeff,q.L,q.kappa,q.basis,q.tk)
  localrows[digits]=MPChunkStore(OUT/('local_'+str(digits)),len(indices),digits,4,dict(basebindings,selected_indices=json.dumps(indices))).run(lambda j:model.jet(float(x[indices[j]]),float(y[indices[j]])),lambda n:print('LOCAL_MP',digits,n,'of',len(indices),now(),flush=True))
 local=compare_decimal_rows(localrows[72],localrows[108],own[indices],'1e-60','1e-52')
 plocal=compare_decimal_rows([z[:3]for z in localrows[72]],[z[:3]for z in localrows[108]],prod[indices],'1e-60','1e-52')
 localout=dict(indices=indices,local=local,producer=plocal,rows72=localrows[72],rows108=localrows[108],bindings=basebindings,scope='Selected local MP jets only; precision disagreement retained, no enclosure.')
 save(OUT/'LOCAL_COMPLETE.json',localout)
 jet=CartesianQJet(q).jet;results=[]
 for index in witnesses:
  xx,yy=float(x[index]),float(y[index]);ck('positive witness coordinates '+str(index),xx>0 and yy>0);geometry=frozen_geometry(jet,xx,yy,q.p,RULES['B']);ref=np.r_[B['velocity'][index],B['Phi'][index],B['dV2dy'][index],B['tail_velocity'][index]]
  ck('bitwise B replay '+str(index),geometry['reference'].tobytes()==ref.tobytes()and geometry['metadata'].tobytes()==B['metadata'][index].tobytes())
  ck('finite B geometry '+str(index),all(np.isfinite(z).all()for z in geometry.values())and np.all(geometry['weight']>0)and np.all(geometry['node']>0))
  path=OUT/('geometry_'+str(index)+'.npz');meta=dict(index=index,rule=RULES['B'],bindings=basebindings);arrays=dict(geometry,manifest=np.array(json.dumps(meta,sort_keys=True)))
  if path.exists():
   previous=load(path);ck('existing geometry exact '+str(index),set(previous)==set(arrays)and all(previous[k].dtype==arrays[k].dtype and previous[k].shape==arrays[k].shape and previous[k].tobytes()==arrays[k].tobytes()for k in arrays))
  else:
   tmp=path.with_suffix('.npz.tmp')
   with tmp.open('wb')as f:np.savez_compressed(f,**arrays)
   tmp.replace(path)
  gb=dict(basebindings);gb[str(path)]=sha(path);rows={};node=geometry['node']
  for digits in [72,108]:
   with mp.workdps(digits):model=ScalarMPDensity(q.coeff,q.L,q.kappa,q.basis,q.tk)
   def integrand(j):
    a=mp.mpf(xx);b=mp.mpf(float(node[j]));return [mp.diff(lambda z:model.density(z,b),a,addprec=40),mp.diff(lambda z:model.density(z,b),a,2,addprec=40)]
   rows[digits]=MPChunkStore(OUT/('integrand_'+str(index)+'_'+str(digits)),len(node),digits,2,gb).run(integrand,lambda n:print('INTEGRAND_MP',index,digits,n,'of',len(node),now(),flush=True))
  comp=compare_decimal_rows(rows[72],rows[108],geometry['derivatives'],'1e-80','1e-48')
  for label in ['precision_maxima','double_pure_relative_maxima']:
   for z in comp[label]:z.update(phase=int(geometry['phase'][z['index']]),physical_y=float(node[z['index']]))
  md=exact_moments(geometry);ml=exact_moments(geometry,rows[72]);mh=exact_moments(geometry,rows[108]);D=exact_components(md,xx,yy);L=exact_components(ml,xx,yy);H=exact_components(mh,xx,yy);bref=dict(zip(COMPONENT_NAMES,map(F,map(float,ref))));identity=[]
  for k in COMPONENT_NAMES:
   a,b,c=H[k]-bref[k],H[k]-D[k],D[k]-bref[k];ck('recomputed exact component decomposition '+str((index,k)),a==b+c)
   identity.append(dict(component=k,total=str(a),integrand=str(b),finite_arithmetic=str(c),precision_change=str(H[k]-L[k]),B=str(bref[k]),D=str(D[k]),M72=str(L[k]),M108=str(H[k])))
  grad=list(map(F,map(float,own[index,1:3])));total=sum((H[k]-bref[k])*g for k,g in zip(['V1','V2'],grad));integrand=sum((H[k]-D[k])*g for k,g in zip(['V1','V2'],grad));arithmetic=sum((D[k]-bref[k])*g for k,g in zip(['V1','V2'],grad));ck('recomputed exact residual decomposition '+str(index),total==integrand+arithmetic)
  nf=F(float(B['residual'][index,1]));ck('positive stored B normalization '+str(index),nf>0);row=dict(index=index,x=xx,y=yy,geometry=gb,integrand=comp,components=identity,moments={label:{k:str(v)for k,v in m.items()}for label,m in [('D',md),('M72',ml),('M108',mh)]},residual_change=dict(total=str(total),integrand=str(integrand),finite_arithmetic=str(arithmetic),B_Nf_stored_float=str(nf),total_over_B_Nf=str(total/nf)if nf else None,scope='Held own binary64 local gradient; normalization uses stored binary64 Nf, not its pre-rounding Fraction.'))
  results.append(row);save(OUT/('witness_'+str(index)+'.json'),row)
 for p,h in basebindings.items():ck('stable '+p,sha(p)==h)
 # Final records bind every complete data artifact, including individual chunks.
 artifacts={str(p):sha(p)for p in OUT.rglob('*')if p.is_file()and p.name!='MP_COMPLETE.json'and not p.name.endswith('.tmp')}
 out=dict(status='COMPLETE_FINITE_MP_SENSITIVITY_REQUIRES_FINAL_REVIEW',started_utc=start,finished_utc=now(),elapsed_seconds=time.perf_counter()-tick,count=len(checks),checks=checks,bindings=basebindings,artifacts=artifacts,local_summary=local,producer_local_summary=plocal,results=results,local_indices=indices,integrand_indices=witnesses,precision_diagnostics_passed=bool(local['precision_diagnostic_passed']and all(z['integrand']['precision_diagnostic_passed']for z in results)),exact_component_identity_count=6*len(results),exact_residual_identity_count=len(results),bookkeeping_identity_count=sum(z['name'].startswith('recomputed exact ')for z in checks),identity_scope='Algebraic bookkeeping, not evidence of derivative or inverse accuracy.',scope='Finite binary64-node MP sensitivity only; no quadrature enclosure, no historical-map authentication, auxiliary hydrostatic only; primary full-plane IPM unresolved.')
 save(OUT/'MP_COMPLETE.json',out);print(out['status'],now(),flush=True)
except Exception:
 save(OUT/'FAILURE.json',dict(started_utc=start,utc=now(),checks=checks,bindings=bindings,traceback=traceback.format_exc()));raise
