"""Independent full-plane inversion and characteristic reconstruction of saved data."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib,shutil,sys
import numpy as np
from adaptive_modal_inverse import AdaptiveModalInverse,ModalSettings,R2ModeSource
from r2_state_values import R2State
from smooth_modal_flow import SmoothModalFlow,reconstruct
from finite_difference import derivative
root=Path(sys.argv[1]);root.mkdir(exist_ok=True,parents=True)
source=Path(sys.argv[2])
snapshot=root/'state_snapshot.npz'
if not snapshot.exists():shutil.copyfile(source,snapshot)
s=R2State(snapshot);src=R2ModeSource(s);ext=R2ModeSource(s,True);eps=float(s.meta['eps']);a0=s.center()['F']['value']
def mixed(r):return eps*src(r)+(1-eps)*ext(r)
inv=AdaptiveModalInverse(mixed,s.K,ModalSettings(1/s.bb,2e-13,2e-12))
tm=s.edges[1:-1];rk=s.L*np.sqrt(np.expm1(-2*s.bb*np.log1p(-tm)))
coarse=np.unique(np.r_[np.geomspace(1e-5,1e3,321),rk[(rk>1e-5)&(rk<1e3)]])
radii=np.sort(np.r_[coarse,np.sqrt(coarse[:-1]*coarse[1:])])
start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','snapshot_sha256':s.sha256,'metadata':s.meta,'center':s.center(),'source':'eps*stored_Omega+(1-eps)*stored_external_Omega','rmin':float(radii[0]),'rmax':float(radii[-1]),'fine_nodes':len(radii),'coarse_nodes':len(coarse),'validation':[],'reconstruction':[]}
def save():
 out['elapsed_seconds']=time.monotonic()-start;(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
pr=[];dp=[];HH=[]
cache=root/'inverse_nodes.npz'
if cache.exists():
 with np.load(cache,allow_pickle=False) as z:
  assert np.array_equal(z['radii'],radii);pr=z['pr'];dp=z['dp'];HH=z['H']
 out['reused_cached_nodes']=True
else:
 for i,r in enumerate(radii):
  inv.settings.epsabs=2e-12*min(r,.1)
  p,d=inv.radial(r);pr.append(p);dp.append(d);HH.append(mixed(r))
  if i%50==0:out['nodes_completed']=i+1;save();print('nodes',i+1,'/',len(radii),'seconds',time.monotonic()-start,flush=True)
 pr=np.array(pr);dp=np.array(dp);HH=np.array(HH)
 np.savez_compressed(cache,radii=radii,pr=pr,dp=dp,H=HH)
 out['node_quadrature']=inv.evidence
fine=SmoothModalFlow(s.beta,radii,pr,dp,HH);coarseflow=SmoothModalFlow(s.beta,radii[::2],pr[::2],dp[::2],HH[::2])
points=np.array([[2.6682490368690326,1.7828670070846302],[3.099729223471515,.8305699421843431],[1.,1.],[.25,3.]])
# Independent inverse at non-node radii. Finite differences use only that inverse.
valpoints=np.r_[points,np.array([[r*np.cos(th),r*np.sin(th)] for r in np.geomspace(2e-4,200,15) for th in [.29,1.12]])]
for X in valpoints:
 inv.settings.epsabs=2e-13
 direct=s.beta*X+inv.relative(X[None])[0];W,D,om=fine.values(X);Wc,Dc,omc=coarseflow.values(X)
 exactsource=float(s.mixed_omega(*X));row={'point':X.tolist(),'velocity_fine_error':float(max(abs(W-direct))),'velocity_coarse_error':float(max(abs(Wc-direct))),'source_fine_error':abs(om-exactsource),'source_coarse_error':abs(omc-exactsource),'DW_resolution_difference':float(np.max(abs(D-Dc))),'divV':float(np.trace(D)-2*s.beta)}
 out['validation'].append(row)
for X in points[:3]:
 hs=1e-5*max(1.,np.linalg.norm(X))
 def component(j):
  def fun(x,y):
   shape=np.shape(x);p=np.column_stack((np.ravel(x),np.ravel(y)))
   return (s.beta*p+inv.relative(p))[:,j].reshape(shape)
  return fun
 Dfd=np.array([[derivative(component(j),X[None],ax,hs)[0] for ax in [0,1]] for j in [0,1]])
 out.setdefault('independent_DW_checks',[]).append({'point':X.tolist(),'relative_step':1e-5,'max_error':float(np.max(abs(Dfd-fine.DW(X)))),'DW_fine':fine.DW(X).tolist(),'DW_fd':Dfd.tolist()})
save();print('interpolation validation complete',time.monotonic()-start,flush=True)
for X in points:
 hs=1e-5*max(1.,np.linalg.norm(X));storedgrad=np.array([derivative(s.theta,X[None],j,hs)[0] for j in [0,1]])
 for resolution,flow,delta,rtol,atol in [('coarse',coarseflow,.001,1e-10,1e-13),('fine',fine,.003,1e-10,1e-13),('fine',fine,.001,1e-10,1e-13),('fine',fine,.0003,1e-10,1e-13),('fine',fine,.001,1e-12,1e-15)]:
  row=reconstruct(flow,X,s.beta,a0,cutoff=delta,rtol=rtol,atol=atol,compatible_seed=True)
  row.update(resolution=resolution,stored_Theta=float(s.theta(*X)),stored_Omega=float(s.omega(*X)),stored_gradient=storedgrad.tolist())
  if row['status']=='COMPLETE':
   row['Theta_difference']=row['Theta']-row['stored_Theta'];row['Omega_difference']=row['Omega']-row['stored_Omega'];row['gradient_difference']=(np.array(row['gradient'])-storedgrad).tolist()
  out['reconstruction'].append(row);save()
 print('point',X.tolist(),'seconds',time.monotonic()-start,flush=True)
out['additional_quadrature']=inv.evidence[out.get('nodes_completed',0):]
out['code_hashes']={p:hashlib.sha256(Path('code_independent',p).read_bytes()).hexdigest() for p in ['characteristic_refined_state.py','adaptive_modal_inverse.py','r2_state_values.py','smooth_modal_flow.py','finite_difference.py']}
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),scope='Finite-cutoff diagnostic for a forced saved field. No interval bounds, global basin certification, coupled solution, or cutoff-limit theorem for an imperfect center strain.')
snap=root/'code_snapshot';snap.mkdir(exist_ok=True)
for name in out['code_hashes']:shutil.copyfile(Path('code_independent',name),snap/name)
save();print('COMPLETE',out['elapsed_seconds'],flush=True)
