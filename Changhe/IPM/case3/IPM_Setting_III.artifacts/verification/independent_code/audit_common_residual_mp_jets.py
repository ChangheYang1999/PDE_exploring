"""Result287 high-precision independent local differentiation, queued CPU work."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,traceback,resource
import mpmath as mp
import numpy as np
import torch
from scalar_mp_hydrostatic_density import ScalarMPDensity
from q_local_checkpoint import QLocalCheckpoint
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3));torch.set_num_threads(1)
R=Path('research/hydrostatic_common_residual_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat();checks=[];rows=[];manufactures=[]
out=dict(status='RUNNING',started_utc=utc(),checks=checks,rows=rows,manufactures=manufactures,proof_sha256=sha(R/'HIGH_PRECISION_JET_PROOF.md'),review_proof_sha256=sha(R/'MP_REVIEW_RESOLUTION.md'),modules={f:sha(Path('independent_code')/f)for f in ['q_local_checkpoint.py','q_checkpoint_reader.py','independent_hydrostatic.py']},driver_sha256=sha(__file__),module_sha256=sha('independent_code/scalar_mp_hydrostatic_density.py'),source_sha256={str(V/f):sha(V/f)for f in ['INPUTS.json','RUN.json','SUMMARY.json','POINTS.npz']})
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def save():
 out['updated_utc']=utc();(V/'MP_JETS.json').write_text(json.dumps(out,indent=2)+'\n')
def dec(a):return[mp.nstr(x,mp.mp.dps)for x in a]
save()
try:
 manufacture=json.loads((V/'MP_EXTENDED_MANUFACTURES.json').read_text());ck('extended manufacture complete',manufacture['status']=='PASS' and all(t['passed']for t in manufacture['checks']));ck('extended manufacture module',manufacture['module_sha256']==out['module_sha256']);ck('extended manufacture driver',manufacture['driver_sha256']==sha('independent_code/check_common_residual_mp_manufactures.py'));ck('extended manufacture proof',manufacture['proof_sha256']==sha(R/'EXTENDED_MP_MANUFACTURE_PROOF.md'));out['extended_manufacture_sha256']=sha(V/'MP_EXTENDED_MANUFACTURES.json');ck('jet layout definition','return np.stack([rho,gx,gy,gxx],axis=-1)'in Path('independent_code/independent_hydrostatic.py').read_text())
 for P in [1.5,2.]:
  with mp.workdps(72):
   model=ScalarMPDensity([[1.]],1.3,P);C=2**(2*model.P)/model.L**2
   for x0,y0 in [(0.,0.),(0.,.1),(.1,0.),(.2,.3),(-.2,.3),(.2,-.3),(3.,4.)]:
    x,y=mp.mpf(x0),mp.mpf(y0);w=model.weight(x*x+y*y);D=1+2*model.P*C*(x*x+y*y)*w**(2*model.P-1);wx=-2*C*x*w**(2*model.P)/D;wy=-2*C*y*w**(2*model.P)/D;wxx=-(2*C*w**(2*model.P)+8*model.P*C*x*w**(2*model.P-1)*wx+2*model.P*(2*model.P-1)*C*(x*x+y*y)*w**(2*model.P-2)*wx*wx)/D;exact=[y*w,y*wx,w+y*wy,y*wxx];got=model.jet(x,y);error=max(abs(a-b)/(1+abs(b))for a,b in zip(got,exact));ck('closed derivative '+str((P,x0,y0)),error<mp.mpf('1e-55'),mp.nstr(error,12));manufactures.append(dict(P=P,x=x0,y=y0,jet=dec(got),exact=dec(exact),error=mp.nstr(error,20)))
 save();s=json.loads((V/'SUMMARY.json').read_text());run=json.loads((V/'RUN.json').read_text());inp=json.loads((V/'INPUTS.json').read_text());ck('summary complete',s['status']=='PASS'and all(t['passed']for t in s['checks']));items={t['tag']:t for t in inp['states']};points=np.load(V/'POINTS.npz')['points'];ck('point shape and dtype',points.shape==(333,4)and points.dtype==np.dtype('float64'));selected={};out['coverage']='18-point union of fixed-rule maximizers disputed in original and revision153 printed tables; no MP inverse or all-grid differentiation.'
 for t in s['disagreements']:selected.setdefault(t['tag'],set()).add(t['index'])
 extension=json.loads((V/'MP_SELECTION.json').read_text());revision=json.loads((V/'revision153/FIXED_COMPARISON.json').read_text());ck('revision fixed complete',revision['status']=='PASS'and all(t['passed']for t in revision['checks']));ck('revision driver binding',revision['driver_sha256']==sha('independent_code/audit_common_residual_revision153.py'));ck('revision input binding',revision['input_sha256']==sha(V/'revision153/INPUTS.json'));ck('extension summary binding',extension['summary_sha256']==sha(V/'SUMMARY.json'));ck('extension revision binding',extension['revision_fixed_sha256']==sha(V/'revision153/FIXED_COMPARISON.json'))
 for t in revision['comparisons']:
  if not t['fixed_agrees']:selected.setdefault(t['tag'],set()).add(t['index'])
 ck('exact18 point union',sorted((tag,i)for tag,indices in selected.items()for i in indices)==[(t['tag'],t['index'])for t in extension['selection']]and len(extension['selection'])==18);out['selection_extension_proof_sha256']=sha(R/'MP_SELECTION_EXTENSION_PROOF.md');out['selection_sha256']=sha(V/'MP_SELECTION.json');out['revision_sha256']=sha(V/'revision153/FIXED_COMPARISON.json');out['revision_input_sha256']=sha(V/'revision153/INPUTS.json')
 for tag,indices in selected.items():
  item=items[tag];ck('state hash '+tag,sha(item['state']['path'])==item['state']['sha256'])
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(item['state']['path'])
  ck('binary64 representation '+tag,all(row.dtype==np.dtype('float64')for row in q.coeff)and q.tk.dtype==np.dtype('float64')and all(type(z)is float for z in [q.L,q.kappa,q.cl]));
  last=next(t['levels'][-1]for t in run['states']if t['tag']==tag);ck('fixed raw hash '+tag,sha(last['path'])==last['sha256']);ff=dict(np.load(last['path']));ck('fixed jet schema '+tag,ff['jets'].shape==(333,4)and ff['velocity'].shape==(333,2)and ff['jets'].dtype==np.dtype('float64'));out.setdefault('state_scalars',{})[tag]={key:float(value).hex()for key,value in [('L',q.L),('P',q.kappa),('c',q.cl)]}
  for i in sorted(indices):
   x,y,r,j=points[i];values=[];record=dict(tag=tag,index=i,x=float(x),y=float(y),precisions=[],coordinate_hex=[float(x).hex(),float(y).hex()]);rows.append(record)
   for dps in [72,108]:
    with mp.workdps(dps):
     print('START',tag,i,dps,utc(),flush=True);model=ScalarMPDensity(q.coeff,q.L,q.kappa,q.basis,q.tk);jet=model.jet(float(x),float(y));ck(tag+' exactly four MP components '+str(i)+' '+str(dps),len(jet)==4);values.append(jet);g,gx,gy,gxx=jet;u,v=map(lambda a:mp.mpf(float(a)),ff['velocity'][i]);xx,yy=mp.mpf(float(x)),mp.mpf(float(y));c=mp.mpf(q.cl);aa=(c*xx+u)*gx;bb=(c*yy+v)*gy;rh=aa+bb-g;nf=abs(aa)+abs(bb)+abs(g);nv=abs(g)+abs(xx*gx+yy*gy)+abs(u*gx+v*gy);nb=mp.sqrt((c*xx+u)**2+(c*yy+v)**2)*mp.sqrt(gx*gx+gy*gy)+abs(g);record['precisions'].append(dict(dps=dps,jet=dec(jet),Rh=mp.nstr(rh,dps),Nf=mp.nstr(nf,dps),Nv=mp.nstr(nv,dps),Nbound=mp.nstr(nb,dps),Rf=mp.nstr(abs(rh)/nf,dps)if nf else None,Rv=mp.nstr(abs(rh)/nv,dps)if nv else None,Rbound=mp.nstr(abs(rh)/nb,dps)if nb else None));save();print('DONE',tag,i,dps,utc(),flush=True)
   with mp.workdps(108):
    relative=[abs(a-b)/(abs(a)+abs(b))if a or b else mp.mpf(0)for a,b in zip(*values)];ck(tag+' component-relative precision '+str(i),max(relative)<mp.mpf('1e-55'),[mp.nstr(t,15)for t in relative]);record['component_relative_precision_difference']=[mp.nstr(t,25)for t in relative];density_error=abs(values[-1][0]-mp.mpf(float(ff['jets'][i,0])));density_tolerance=mp.mpf(65536)*mp.mpf(float(np.finfo(float).eps))*(1+abs(values[-1][0]));ck(tag+' density consistency '+str(i),density_error<=density_tolerance,dict(error=mp.nstr(density_error,20),tolerance=mp.nstr(density_tolerance,20),scope='Empirical arithmetic consistency tolerance, not a bound'));difference=max(abs(a-b)/(1+abs(b))for a,b in zip(*values));ck(tag+' precision '+str(i),difference<mp.mpf('1e-55'),mp.nstr(difference,15));delta=[float(v-mp.mpf(float(w)))for v,w in zip(values[-1],ff['jets'][i])];record['double_jet_difference']=delta;record['maximum_scaled_double_jet_difference']=float(max(abs(v-mp.mpf(float(w)))/(1+abs(v))for v,w in zip(values[-1],ff['jets'][i])));record['local_Rh_change_with_fixed_velocity']=float(mp.mpf(record['precisions'][-1]['Rh'])-mp.mpf(float(ff['Rh'][i])));record['local_Rf_change_with_fixed_velocity']=float(mp.mpf(record['precisions'][-1]['Rf'])-mp.mpf(float(ff['Rf'][i])));ck(tag+' finite local differences '+str(i),np.isfinite(delta).all());save()
 out.update(status='PASS',count=len(checks),finished_utc=utc());save();print('PASS',len(checks),len(rows),utc(),flush=True)
except Exception:
 out.update(status='FAIL',count=len(checks),finished_utc=utc(),traceback=traceback.format_exc());save();raise
