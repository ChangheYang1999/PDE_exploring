"""P210: selected input-Jacobian actions through this lane's own inverse.

Only NUM data are read. No fitting-lane code imports or solver execution.
Single-threaded; checkpoint every 20 inverse nodes and every response.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import json, hashlib, time, os, traceback, resource
import numpy as np
from scipy.interpolate import BSpline
from r2_state_values import R2State
from adaptive_modal_inverse import AdaptiveModalInverse, ModalSettings, R2ModeSource
from smooth_modal_flow import SmoothModalFlow, reconstruct
from cartesian_inverse import CartesianInverse, InverseSettings
from native_coefficient_values import divided_values

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/210_independent_jacobian_actions/verification'
SOURCE=ROOT/'research/197_vertex_mapscale_audit/verification/certificates/archives/mbb_b3.0952_lambda0.989973.npz'
MATRIX=ROOT/'research/208_saved_jacobian_audit/verification/frozen_sources/jac_L2v.npz'
DIAG=ROOT/'research/208_saved_jacobian_audit/verification/recomputed_matrix_diagnostics.npz'
GRAM=ROOT/'research/205_physical_gram_and_strain_norm/verification/native_gram.npz'
BASE=ROOT/'research/200_projected_characteristic_response/verification/native_inverse_nodes.npz'
PV=ROOT/'research/200_projected_characteristic_response/verification/projection_vectors.npz'
POINTS=np.array([[.2,.1],[.8,.4],[1.,1.],[.3,3.],[3.,1.]])

def now():return datetime.now(timezone.utc).isoformat()
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def dump(path,data):
 tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(data,indent=2)+'\n');tmp.replace(path)
def vec(row):return np.array([row['Theta'],*row['gradient'],row['Omega']])

def main():
 OUT.mkdir(parents=True,exist_ok=True);start=time.monotonic()
 s=R2State(SOURCE);lam=float(s.meta['lam']);a0=float(s.meta['a0'])
 with np.load(MATRIX,allow_pickle=False) as z:
  JT=z['JT'];active=z['act_idx'];z0=z['x_star'];cv=z['Vweak'][-1];matrixq=z['c_act']
 with np.load(DIAG,allow_pickle=False) as z:hv=z['physical_weak_coefficients'][-1]
 with np.load(GRAM,allow_pickle=False) as z:H=z['H'];oldq=z['q'];gramactive=z['active']
 with np.load(BASE,allow_pickle=False) as z:
  radii=z['radii'];pb=z['pr_base'];db=z['dp_base'];hb=z['H_base'];base_source=str(z['source_sha256'])
 with np.load(PV,allow_pickle=False) as z:projected_base=z['projected']
 ints=BSpline(s.knots,np.eye(s.nb),s.degree,extrapolate=False).integrate(0.,1.)
 qfull=np.zeros((s.K,s.nb));qfull[1]=-s.bb*s.L*ints/4
 if s.K>3:qfull[3]=s.bb*s.L*ints/4
 for k in range(s.K):qfull[k,:k//2]=0.
 q=qfull.ravel()[active];q2=float(q@q)
 assert np.array_equal(active,gramactive)
 assert base_source==s.sha256
 assert s.beta==s.bb and float(s.meta['eps'])==1.
 assert np.array_equal(z0,s.rawG.ravel()[active])
 assert np.max(abs(q-oldq))<1e-14 and np.max(abs(q-matrixq))<2e-14
 cf=float(s.strain('native_seed'));cstar=1+s.beta/2
 projected=z0+q*(cstar-q@z0-lam*cf)/q2
 assert np.max(abs(projected-projected_base[active]))<5e-14
 files=[SOURCE,MATRIX,DIAG,GRAM,BASE,PV,ROOT/'research/210_independent_jacobian_actions/PROOF.md']
 files += [ROOT/'code_independent'/f for f in ['independent_jacobian_actions.py','r2_state_values.py','native_coefficient_values.py','smooth_modal_flow.py','adaptive_modal_inverse.py','cartesian_inverse.py']]
 out={'started_utc':now(),'status':'RUNNING','pid':os.getpid(),'priority':os.getpriority(os.PRIO_PROCESS,0),
  'source_sha256':s.sha256,'input_hashes':{str(f.relative_to(ROOT)):sha(f) for f in files},
  'a0':a0,'stored_F_center':s.center()['F']['value'],'beta':s.beta,'lambda':lam,
  'norm':'full-plane integral [r^(1/4)+r^(-1/4)] |G|^2 dX, R=1',
  'map':'input coefficients; affine strain projection; fixed beta, lambda, source, a0; canonical relative full-plane velocity; finite-cutoff scalar output',
  'proof_file':'research/210_independent_jacobian_actions/PROOF.md','checks':[],'directions':[],
  'base_cache':'P200 own modal whole-plane nodes; exact same projected input state',
  'scope':'Sampled finite-cutoff directional derivatives versus the physical value of a fitted coefficient array action. No norm enclosure, cutoff-limit theorem or nonlinear fixed point.'}
 def save():
  out.update(updated_utc=now(),elapsed_seconds=time.monotonic()-start,max_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
  dump(OUT/'actions.json',out)
 def check(name,error,tol):
  err=float(error);out['checks'].append({'name':name,'error':err,'tolerance':tol,'pass':bool(err<=tol)})
  if err>tol:raise RuntimeError(f'control {name} failed: {err} > {tol}')
 # Exact finite-difference polynomial moments.
 weights=[Fraction(1,12),Fraction(-8,12),Fraction(8,12),Fraction(-1,12)]
 for k in range(5):check(f'exact_four_point_polynomial_degree_{k}',abs(sum(w*j**k for w,j in zip(weights,[-2,-1,1,2]))-(1 if k==1 else 0)),0)
 check('projection_idempotence_vector',np.linalg.norm((cv-q*(q@cv)/q2)-q*(q@(cv-q*(q@cv)/q2))/q2-(cv-q*(q@cv)/q2)),1e-13)
 check('removed_q',np.linalg.norm(q-q*(q@q)/q2),1e-14)
 check('projected_base_strain',abs(q@projected+lam*cf-cstar),2e-12)
 check('base_cache_projection',np.max(abs(projected-projected_base[active])),5e-14)
 for step in [1e-4,2e-4]:
  explicit=z0+step*cv+q*(cstar-q@(z0+step*cv)-lam*cf)/q2
  check(f'affine_projection_step_{step}',np.max(abs(explicit-projected-step*(cv-q*(q@cv)/q2))),1e-13)
 # A linear observable must yield Jv without a transpose or sign change.
 Ltest=np.array([[1.,2.,-3.],[-2.,.5,4.]]);vt=np.array([.3,-.4,.2]);zt=np.array([.8,.7,-.2]);h=.125
 linear_rows=[Ltest@(zt+j*h*vt) for j in [-2,-1,1,2]]
 check('linear_observable_action_orientation',np.max(abs((linear_rows[0]-8*linear_rows[1]+8*linear_rows[2]-linear_rows[3])/(12*h)-Ltest@vt)),5e-15)
 for h in [.1,.05]:
  vals=np.exp(np.array([-2,-1,1,2])*h)
  err=abs((vals[0]-8*vals[1]+8*vals[2]-vals[3])/(12*h)-1)
  out['checks'].append({'name':f'exp_difference_step_{h}','error':float(err),'tolerance':h**4/20,'pass':bool(err<h**4/20)})
 assert all(c['pass'] for c in out['checks'])
 finebase=SmoothModalFlow(s.beta,radii,pb,db,hb);coarsebase=SmoothModalFlow(s.beta,radii[::2],pb[::2],db[::2],hb[::2])
 decay=1/s.bb
 for label,vraw in [('coefficient_weakest',cv),('physical_weakest',hv)]:
  v=vraw/np.sqrt(vraw@H@vraw);d=v-q*(q@v)/q2;jv=JT@v
  drecord={'label':label,'input_norm_H':float(np.sqrt(v@H@v)),
   'input_norm_coefficient':float(np.linalg.norm(v)),'input_strain':float(q@v),'projected_strain':float(q@d),
   'projected_norm_H':float(np.sqrt(d@H@d)),'projected_norm_coefficient':float(np.linalg.norm(d)),
   'Jv_norm_H':float(np.sqrt(jv@H@jv)),'Jv_norm_coefficient':float(np.linalg.norm(jv)),
   'Av_norm_H':float(np.sqrt((jv-v)@H@(jv-v))),
   'node_evidence':[],'interpolation_validation':[],'cartesian_inverse':[],'responses':[],'stage':'inverse_nodes'}
  check(label+'_projected_zero_strain',abs(q@d),5e-14)
  check(label+'_unit_norm_H',abs(v@H@v-1),2e-13)
  out['directions'].append(drecord);save()
  ddir=OUT/label;ddir.mkdir(exist_ok=True)
  np.savez_compressed(ddir/'vectors.npz',v=v,projected_direction=d,JT_action=jv,active=active,q=q)
  with np.load(SOURCE,allow_pickle=False) as z:archive={k:z[k].copy() for k in z.files}
  cfull=np.zeros(s.K*s.nb);cfull[active]=d
  archive['cG']=cfull.reshape(s.rawG.shape);archive['lam']=np.array(0.)
  np.savez_compressed(ddir/'direction_state.npz',**archive)
  sd=R2State(ddir/'direction_state.npz');modes=R2ModeSource(sd)
  inv=AdaptiveModalInverse(modes,s.K,ModalSettings(decay,2e-13,2e-11))
  vals=[[],[],[]];nodes=ddir/'inverse_nodes.npz'
  if nodes.exists():
   with np.load(nodes,allow_pickle=False) as z:
    assert np.array_equal(z['radii'],radii)
    assert np.array_equal(z['projected_direction'],d)
    vals=[list(z[k]) for k in ['pr','dp','H']]
   drecord['reused_nodes']=len(vals[0])
  def save_nodes():np.savez_compressed(nodes,radii=radii,projected_direction=d,pr=np.asarray(vals[0]),dp=np.asarray(vals[1]),H=np.asarray(vals[2]))
  for i in range(len(vals[0]),len(radii)):
   r=float(radii[i]);inv.settings.epsabs=2e-12*min(r,.1)
   pdir,ddirv=inv.radial(r)
   for ar,val in zip(vals,[pdir,ddirv,modes(r)]):ar.append(val)
   drecord['node_evidence'].append(inv.evidence[-1])
   if i%20==0 or i+1==len(radii):
    drecord['nodes_completed']=i+1;save_nodes();save();print(now(),label,'nodes',i+1,'/',len(radii),'elapsed',out['elapsed_seconds'],flush=True)
  pd,dd,hd=map(np.asarray,vals)
  flowcache={}
  def flow(h=0.,grid='fine'):
   key=(float(h),grid)
   if key not in flowcache:
    sl=slice(None,None,2 if grid=='coarse' else 1)
    flowcache[key]=SmoothModalFlow(s.beta,radii[sl],(pb+h*pd)[sl],(db+h*dd)[sl],(hb+h*hd)[sl])
   return flowcache[key]
  dirflow=SmoothModalFlow(0.,radii,pd,dd,hd);dircoarse=SmoothModalFlow(0.,radii[::2],pd[::2],dd[::2],hd[::2])
  drecord['stage']='inverse_validation';save()
  valpoints=np.r_[POINTS,[[r*np.sin(phi),-r*np.cos(phi)] for r in [.0004,.004,.04,.4,4.,20.] for phi in [.37,1.61,2.43]]]
  for X in valpoints:
   inv.settings.epsabs=2e-13
   exact=inv.relative(X[None])[0];vf,dvf,of=dirflow.values(X);vc,dvc,oc=dircoarse.values(X)
   drecord['interpolation_validation'].append({'point':X.tolist(),'fine_velocity_error':abs(vf-exact).tolist(),
    'coarse_velocity_error':abs(vc-exact).tolist(),'DW_resolution_difference':float(np.max(abs(dvf-dvc))),
    'fine_source_error':float(abs(of-sd.omega(*X))),'coarse_source_error':float(abs(oc-sd.omega(*X))),
    'divergence_error':float(abs(np.trace(dvf)))})
  for order in [12,18]:
   points=POINTS[[0,2,4]];exact=inv.relative(points)
   settings=InverseSettings(radius=12.,core_radial_order=order,core_angular_order=3*order,
    exterior_radial_order=4*order,exterior_angular_order=4*order,decay_power=decay)
   cart=CartesianInverse(sd.omega,settings).relative(points)
   drecord['cartesian_inverse'].append({'order':order,'points':points.tolist(),'modal':exact.tolist(),'cartesian':cart.tolist(),
    'absolute_component_errors':abs(cart-exact).tolist(),'settings':settings.__dict__})
   save();print(now(),label,'Cartesian',order,'max_error',float(np.max(abs(cart-exact))),flush=True)
  drecord['stage']='characteristics';save();cache={}
  def evaluate(X,h,cutoff,grid,tol):
   key=(*X,float(h),float(cutoff),grid,float(tol))
   if key not in cache:
    f=flow(h,grid)
    row=reconstruct(f,X,s.beta,a0,cutoff=cutoff,rtol=tol,atol=tol*.01,compatible_seed=True)
    row.update(offset=float(h),grid=grid)
    if row['status']=='COMPLETE':
     seed=np.array(row['seed_point']);row['outgoing_flux']=float(f.W(seed)@seed/np.linalg.norm(seed))
    cache[key]=row
   return cache[key]
  for X in POINTS:
   fitted=float(X[0]*divided_values(s,jv,active,X[None])[0])
   for cutoff,grid,tol,step in [(.001,'fine',1e-10,2e-4),(.001,'fine',1e-10,1e-4),(.0003,'fine',1e-10,1e-4),(.001,'coarse',1e-10,1e-4),(.001,'fine',1e-12,1e-4)]:
    rows=[evaluate(X,j*step,cutoff,grid,tol) for j in [-2,-1,1,2]]
    response={'point':X.tolist(),'cutoff':cutoff,'grid':grid,'rtol':tol,'step':step,'fitted_array_Omega_action':fitted,'evaluations':rows}
    if all(r['status']=='COMPLETE' for r in rows):
     vv=[vec(r) for r in rows];fd4=(vv[0]-8*vv[1]+8*vv[2]-vv[3])/(12*step);fd2=(vv[2]-vv[1])/(2*step)
     den=max(abs(fd4[-1]),abs(fitted));response.update(status='COMPLETE',derivative_Theta_gradient_Omega=fd4.tolist(),
      second_order_difference=fd2.tolist(),difference_to_fitted_Omega=float(fd4[-1]-fitted),
      absolute_gap=float(abs(fd4[-1]-fitted)),relative_gap=float(abs(fd4[-1]-fitted)/den) if den else None,
      denominator=float(den),ratio_zero_rule='null only if both values are exactly zero; no positive floor')
    else:response['status']='FAILED'
    drecord['responses'].append(response);save()
   print(now(),label,'point',X.tolist(),'elapsed',out['elapsed_seconds'],flush=True)
  drecord['inverse_evidence']=inv.evidence;drecord['stage']='COMPLETE';drecord['ended_utc']=now();save()
 out.update(status='COMPLETE',ended_utc=now());save();print(now(),'COMPLETE','elapsed',out['elapsed_seconds'],flush=True)

if __name__=='__main__':
 try:main()
 except Exception:
  OUT.mkdir(parents=True,exist_ok=True)
  (OUT/'failure.txt').write_text(now()+'\n'+traceback.format_exc())
  raise
