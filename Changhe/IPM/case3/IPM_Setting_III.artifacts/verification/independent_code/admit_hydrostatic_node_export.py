"""Finite-byte/source admission; no producer code imported and no inverse evaluated."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,ast,sys,traceback
import numpy as np
import torch
from q_local_checkpoint import QLocalCheckpoint
from node_export_arithmetic_strict import array64,residual,exact

def main():
 r=Path('research/hydrostatic_actual_node_export_audit');v=r/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[];binds={};out=dict(status='RUNNING',started_utc=datetime.now(timezone.utc).isoformat(),checks=checks,bindings=binds)
 def save():out['utc']=datetime.now(timezone.utc).isoformat();(v/'ADMISSION.json').write_text(json.dumps(out,indent=2)+'\n')
 def ck(n,b,e=None):
  checks.append(dict(name=n,passed=bool(b),evidence=e))
  if not b:save();raise AssertionError((n,e))
 def bind(p,h=None):
  p=Path(p);a=sha(p);ck('binding '+str(p),h is None or a==h);binds[str(p)]=a;return p
 try:
  for p in [Path('independent_code/admit_hydrostatic_node_export.py'),r/'ADMISSION_PROOF.md',r/'PROOF.md',r/'DESIGN_REVIEW_RESOLUTION_PROOF.md',v/'EXPORT_INVENTORY.json',v/'PROVENANCE_INPUTS.json',v/'MANUFACTURES_EXPANDED.json',Path('independent_code/q_local_checkpoint.py'),Path('independent_code/q_checkpoint_reader.py'),Path('independent_code/node_export_arithmetic_strict.py'),Path('independent_code/node_export_arithmetic.py')]:bind(p)
  inv=json.loads((v/'EXPORT_INVENTORY.json').read_text());src=json.loads((v/'PROVENANCE_INPUTS.json').read_text());mf=json.loads((v/'MANUFACTURES_EXPANDED.json').read_text())
  ck('completed expanded gates',mf['status']=='PASS_EXPANDED_MANUFACTURES_ONLY'and mf['count']==717==len(mf['checks'])and all(z['passed']for z in mf['checks']))
  for p,h in mf['bindings'].items():bind(p,h)
  for z in src['entries']:bind(z['frozen'],z['sha256']);ck('two-read source '+z['frozen'],z['two_reads_identical'])
  bind(inv['frozen'],inv['sha256']);ck('two-read export inventory',inv['two_reads_identical']and inv['sha256']=='071b990c7a9ee3a91faeca5a1cc8c7d9ef6ef478f41ccd591fbe1ad5575d42d7')
  sp=bind(src['state']['frozen'],src['state']['sha256']);ck('304 state identity',src['state']['sha256']=='4ad484e6391001597ab57d501c8b3f644259af7b4c217b5032a28b00be609d01'and src['state']['two_reads_identical'])
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(sp)
  ck('state dimensions and auxiliary parameters',q.N==96 and q.M==24 and q.cl==2 and q.kappa==2 and q.p==.5 and q.L==1 and q.basis=='local')
  ck('finite coefficient schema',q.u.shape==(2052,)and q.u.dtype==np.dtype('float64')and np.isfinite(q.u).all()and len(q.coeff)==24)
  ck('state construction options',q.data['result']['inner']=='log'and q.data['result']['centre']=='drop'and not q.data['result']['fine']and not q.data['result']['extra'])
  with np.load(inv['frozen'],allow_pickle=False)as z:arrays={k:z[k]for k in z.files}
  vector_keys=['X','Y','V1_map','V2_map','V1_ref','V2_ref','gx','gy','g','F_rows','b_rows'];meta=['N','M','c','quad_map','quad_ref'];ck('exact export key set',set(arrays)==set(vector_keys+meta))
  for k in vector_keys:array64(arrays[k],(2304,));ck('finite native binary64 vector '+k,True)
  for k,want in [('N',96),('M',24)]:ck('integer metadata '+k,arrays[k].shape==()and arrays[k].dtype==np.dtype('int64')and arrays[k].item()==want)
  array64(arrays['c'],());ck('c metadata',arrays['c'].item()==2)
  for k in ['quad_map','quad_ref']:ck('string scalar '+k,arrays[k].shape==()and arrays[k].dtype.kind=='U')
  qm=ast.literal_eval(arrays['quad_map'].item());ck('map quadrature metadata',qm==dict(n_in=24,n_tail=80,hstep='r',inner='log',n0=24,per_decade=4,ngl=8,q=3))
  ck('reference quadrature metadata',arrays['quad_ref'].item()=='hs_layer.hydro_V_log n0=32 per_decade=10 ngl=16 n_tail=400 q=2 hrel=1e-5 (step 1e-5 (1 + r))')
  x,y=arrays['X'],arrays['Y'];ck('positive quadrant no axis witnesses',np.all(x>0)and np.all(y>0))
  th=(np.arange(24)+.5)*np.pi/48;t0=-np.cos(2*np.pi*np.arange(97)/193);coord=[]
  for label,t in [('stored_t',q.tk),('independent_Radau_t',t0)]:
   rr=q.L*np.sqrt((1+t[1:])/2)/(1-t[1:])**q.kappa;xx=(rr[:,None]*np.cos(th)).ravel();yy=(rr[:,None]*np.sin(th)).ravel();row=dict(label=label)
   for key,got,want in [('X',x,xx),('Y',y,yy)]:
    diff=np.abs(got-want);ulps=diff/np.spacing(want);i=int(np.argmax(ulps));row[key]=dict(max_absolute=float(diff.max()),max_ulps=float(ulps[i]),index=i,export_hex=float(got[i]).hex(),reconstructed_hex=float(want[i]).hex(),over_16_ulps=np.flatnonzero(ulps>16).tolist());ck(label+' coordinate '+key,np.all(ulps<=16),row[key])
   coord.append(row)
  out['coordinate_comparisons']=coord;out['export_radial_range']=[float(np.hypot(x,y).min()),float(np.hypot(x,y).max())]
  ck('radial flattening order',np.all(np.diff(np.hypot(x,y).reshape(96,24)[:,0])>0))
  ck('angular flattening order',np.all(np.diff(np.arctan2(y,x).reshape(96,24),axis=1)>0))
  source=(v/'producer_maps_static.py').read_text();tree=ast.parse(source);cl=next(z for z in tree.body if isinstance(z,ast.ClassDef)and z.name=='HSModel');fn=next(z for z in cl.body if isinstance(z,ast.FunctionDef)and z.name=='residual');a={z.targets[0].id:z.value for z in fn.body if isinstance(z,ast.Assign)and len(z.targets)==1 and isinstance(z.targets[0],ast.Name)}
  expr=lambda s:ast.dump(ast.parse(s,mode='eval').body)
  for key,formula in [('R','(c * X + V1) * gx + (c * Y + V2) * gy - g'),('V1',"mp['M1'] @ u"),('V2',"mp['M2'] @ u"),('g',"mp['G'] @ u"),('gx',"mp['Gx'] @ u"),('gy',"mp['Gy'] @ u")]:ck('static residual semantics '+key,ast.dump(a[key])==expr(formula))
  ck('static unweighted first row',isinstance(a['rows'],ast.List)and ast.dump(a['rows'].elts[0])==expr('R'))
  exporter=ast.parse((v/'producer_exporter_static.py').read_text());calls=[z for z in ast.walk(exporter)if isinstance(z,ast.Call)and isinstance(z.func,ast.Attribute)and z.func.attr=='savez_compressed'];ck('one export call',len(calls)==1);kw={z.arg:z.value for z in calls[0].keywords}
  for key,val in [('X','X'),('Y','Y'),('V1_map','V1m'),('V2_map','V2m'),('V1_ref','V1r'),('V2_ref','V2r'),('g','g_nodes'),('gx','gx'),('gy','gy'),('b_rows','b_rows'),('F_rows','F[:len(X)].cpu().numpy()')]:ck('static exported '+key,ast.dump(kw[key])==expr(val))
  flat=' '.join((v/'producer_exporter_static.py').read_text().split());ck('static rebuilt map execution declaration','hsm.build_maps(batch=batch)'in flat and "hsm.residual(u, c, 'drop')"in flat)
  for phrase in ['M1[:, k0:k1] = (-J1).T','M2[:, k0:k1] = (I_in + yv[None] * J2).T','I_in = (W_in[None] * T_in[None] * gxx_in).sum(-1)','J1 = (W_t[None] * gx_t).sum(-1)','J2 = (W_t[None] * gxx_t).sum(-1)']:ck('static inverse recipe '+phrase,phrase in source)
  logs=(v/'producer_export_log.txt').read_text();ck('log associates expected basename','hsG_c2.0_N96_log.pt 96x24 c=2.0 maps'in logs and 'hsG_c2.0_N96_log_nodes_maps.npz'in logs)
  # Exact arithmetic on exported fields only. This establishes data consistency, not inverse truth.
  largest={'F_rows':dict(error=0.,scaled=0.,index=-1),'b_rows':dict(error=0.,scaled=0.,index=-1)};eps=F(1,2**52)
  for i in range(2304):
   jp=[arrays[k][i]for k in ['g','gx','gy']];vm=[arrays[k][i]for k in ['V1_map','V2_map']];vp=[arrays[k][i]for k in ['V1_ref','V2_ref']];z=residual(jp,vm,2,x[i],y[i]);d0=exact(vp[0])-exact(vm[0]);d1=exact(vp[1])-exact(vm[1]);b=d0*exact(jp[1])+d1*exact(jp[2]);bn=abs(d0*exact(jp[1]))+abs(d1*exact(jp[2]))
   for key,want,natural in [('F_rows',z['R'],z['Nf']),('b_rows',b,bn)]:
    error=abs(exact(arrays[key][i])-want);scaled=error/natural if natural else F(0);ck(key+' arithmetic '+str(i),error<=128*eps*natural,dict(error=str(error))if error>128*eps*natural else None)
    if float(scaled)>largest[key]['scaled']:largest[key]=dict(error=float(error),scaled=float(scaled),index=i)
  out['export_arithmetic']=largest;out['metadata']=dict(N=96,M=24,c=2.,L=1.,Pmap=2.,p=.5,basis='local',quad_map=qm,quad_ref=arrays['quad_ref'].item(),flattening='radial major, angle minor',vectors='rebuilt map products and published reference, auxiliary velocity excludes cX',state_association='currently matching checkpoint and source declaration; no embedded coefficient hash or historical authentication',axis_parity='exact recipe only; no exported signed/axis witnesses')
  for p,h in binds.items():ck('unchanged '+p,sha(p)==h)
  out.update(status='PASS_FINITE_EXPORT_ADMISSION_PENDING_REVIEW',count=len(checks),scope='Finite schema, coordinate, static-source and arithmetic consistency. No independent candidate inverse or actual historical matrix verification. Full-plane IPM unresolved.');save();print(out['status'],len(checks),json.dumps(coord))
 except Exception:out.update(status='FAIL',count=len(checks),traceback=traceback.format_exc());save();raise
if __name__=='__main__':main()
