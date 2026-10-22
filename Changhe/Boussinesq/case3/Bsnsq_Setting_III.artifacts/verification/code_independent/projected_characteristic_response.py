"""P200 native-source projected lambda response, no numerics code imports.

One single-thread process. All whole-plane integration is this lane's own
adaptive modal inverse, cross-checked against its independent Cartesian inverse.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, time, os, traceback
import numpy as np
from scipy.interpolate import BSpline
from r2_state_values import R2State
from adaptive_modal_inverse import AdaptiveModalInverse, ModalSettings, R2ModeSource
from smooth_modal_flow import SmoothModalFlow, reconstruct
from cartesian_inverse import CartesianInverse, InverseSettings

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/200_projected_characteristic_response/verification'
SOURCE=ROOT/'research/197_vertex_mapscale_audit/verification/certificates/archives/mbb_b3.0952_lambda0.989973.npz'

def now():return datetime.now(timezone.utc).isoformat()
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def vector(row):return np.array([row['Theta'],*row['gradient'],row['Omega']])

def write_json(path,value):
 temp=path.with_suffix('.tmp');temp.write_text(json.dumps(value,indent=2)+'\n');temp.replace(path)

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 start=time.monotonic();s=R2State(SOURCE);lam=float(s.meta['lam']);a0=float(s.center()['F']['value']);cstar=1+s.beta/2
 if not s.native_source:raise ValueError('expected recorded native source')
 if float(s.meta.get('eps',1.))!=1.:raise ValueError('eps path not included')
 out={'started_utc':now(),'status':'RUNNING','pid':os.getpid(),'priority':os.getpriority(os.PRIO_PROCESS,0),
      'source_path':str(SOURCE.relative_to(ROOT)),'source_sha256':digest(SOURCE),'metadata':s.meta,
      'a0':a0,'parameter':lam,'fixed_beta':s.beta,'derivative_convention':'Fixed unprojected coefficient vector, beta and native forcing field; project total strain at each lambda.',
      'original_center':s.center(),'stage':'projection','code_hashes':{p:digest(ROOT/'code_independent'/p) for p in ['projected_characteristic_response.py','r2_state_values.py','adaptive_modal_inverse.py','smooth_modal_flow.py','cartesian_inverse.py']}}
 def save():
  out['elapsed_seconds']=time.monotonic()-start;out['updated_utc']=now();write_json(OUT/'native_response.json',out)
 ints=BSpline(s.knots,np.eye(s.nb),s.degree,extrapolate=False).integrate(0.,1.)
 q=np.zeros((s.K,s.nb));q[1]=-s.bb*s.L*ints/4
 if s.K>3:q[3]=s.bb*s.L*ints/4
 for k in range(s.K):q[k,:k//2]=0.
 q=q.ravel();q2=float(q@q);cf=float(s.strain('native_seed'));cs=float(s.strain());raw=s.rawG.ravel()
 projected=raw+q*(cstar-cs-lam*cf)/q2;direction=-cf*q/q2
 def archive(path,cG):
  with np.load(SOURCE,allow_pickle=False) as z:obj={k:z[k].copy() for k in z.files}
  obj['cG']=np.reshape(cG,s.rawG.shape);obj['lam']=np.asarray(0.)
  np.savez_compressed(path,**obj)
 archive(OUT/'projected_self.npz',projected);archive(OUT/'direction_self.npz',direction)
 sp=R2State(OUT/'projected_self.npz');sd=R2State(OUT/'direction_self.npz')
 out['projection']={'c_star':cstar,'q_squared':q2,'native_source_strain':cf,
  'original_self_strain':cs,'original_total_strain':cs+lam*cf,
  'projected_self_strain':float(sp.strain()),'total_strain_error':float(sp.strain()+lam*cf-cstar),
  'direction_self_strain':float(sd.strain()),'direction_total_strain':float(sd.strain()+cf),
  'coefficient_change_norm':float(np.linalg.norm(projected-raw)),
  'q_dot_raw_minus_reader_strain':float(q@raw-cs),
  'center_value_change':float(sp.center()['G']['value']-s.center()['G']['value'])}
 if abs(out['projection']['total_strain_error'])>2e-12 or abs(out['projection']['direction_total_strain'])>2e-12:raise RuntimeError('projection control failed')
 np.savez_compressed(OUT/'projection_vectors.npz',q=q,projected=projected,direction=direction,original=raw)
 self_mode=R2ModeSource(sp);dir_mode=R2ModeSource(sd);seed_mode=R2ModeSource(s,kind='native_seed');count=max(s.K,seed_mode.count)
 def pad(v):return np.pad(v,(0,count-len(v)))
 def modes_base(r):return pad(self_mode(r))+lam*pad(seed_mode(r))
 def modes_dir(r):return pad(dir_mode(r))+pad(seed_mode(r))
 decay=min(1/s.bb,1/s.seed_field.bb)
 inv_base=AdaptiveModalInverse(modes_base,count,ModalSettings(decay,2e-13,2e-11))
 inv_dir=AdaptiveModalInverse(modes_dir,count,ModalSettings(decay,2e-13,2e-11))
 # Include both native and unknown spline knots in addition to a physical grid.
 rmin=1e-5;rmax=50.
 grid=list(np.geomspace(rmin,rmax,153))
 for field in [s,s.seed_field]:
  t=field.edges[1:-1];rk=field.L*np.sqrt(np.expm1(-2*field.bb*np.log1p(-t)))
  grid+=rk[(rk>rmin)&(rk<rmax)].tolist()
 logs=np.sort(np.log(grid));keep=np.r_[True,np.diff(logs)>1e-9];coarse=np.exp(logs[keep])
 radii=np.sort(np.r_[coarse,np.sqrt(coarse[:-1]*coarse[1:])]);nodes=OUT/'native_inverse_nodes.npz'
 out.update(stage='inverse_nodes',coarse_nodes=len(coarse),fine_nodes=len(radii),rmin=rmin,rmax=rmax,
  inverse_settings={'decay_mapping':decay,'epsrel':2e-11,'epsabs_rule':'2e-12*min(r,0.1)','full_plane':True},node_evidence=[])
 vals=[[],[],[],[],[],[]]
 if nodes.exists():
  with np.load(nodes,allow_pickle=False) as z:
   if not np.array_equal(z['radii'],radii):raise ValueError('cached grid differs')
   if str(z['source_sha256'])!=s.sha256:raise ValueError('cached source differs')
   vals=[list(z[key]) for key in ['pr_base','dp_base','H_base','pr_dir','dp_dir','H_dir']]
  out['reused_nodes']=len(vals[0])
 def save_nodes():
  np.savez_compressed(nodes,radii=radii,source_sha256=np.asarray(s.sha256),
   **dict(zip(['pr_base','dp_base','H_base','pr_dir','dp_dir','H_dir'],[np.asarray(v) for v in vals])))
 for i in range(len(vals[0]),len(radii)):
  r=radii[i]
  for inv in [inv_base,inv_dir]:inv.settings.epsabs=2e-12*min(r,.1)
  pb,db=inv_base.radial(r);pd,dd=inv_dir.radial(r)
  for v,item in zip(vals,[pb,db,modes_base(r),pd,dd,modes_dir(r)]):v.append(item)
  out['node_evidence'].append({'index':i,'base':inv_base.evidence[-1],'direction':inv_dir.evidence[-1]})
  if i%20==0 or i+1==len(radii):
   out['nodes_completed']=i+1;save_nodes();save();print(now(),'nodes',i+1,'/',len(radii),'seconds',out['elapsed_seconds'],flush=True)
 pb,db,hb,pd,dd,hd=[np.asarray(v) for v in vals]
 def flow(h=0.,coarse=False):
  sl=slice(None,None,2 if coarse else 1)
  return SmoothModalFlow(s.beta,radii[sl],(pb+h*pd)[sl],(db+h*dd)[sl],(hb+h*hd)[sl])
 fine=flow();coarseflow=flow(coarse=True);directionflow=SmoothModalFlow(0.,radii,pd,dd,hd)
 points=np.array([[.2,.1],[.8,.4],[1.,1.],[.3,3.],[3.,1.]])
 validate=np.r_[points,[[r*np.sin(phi),-r*np.cos(phi)] for r in [.0004,.004,.04,.4,4.,20.] for phi in [.37,1.61,2.43]]]
 out.update(stage='inverse_validation',interpolation_validation=[]);save()
 def omega_base(x,y):return sp.omega(x,y)+lam*np.asarray(x)*s.divided(x,y,'native_seed')
 def omega_dir(x,y):return sd.omega(x,y)+np.asarray(x)*s.divided(x,y,'native_seed')
 for X in validate:
  for inv in [inv_base,inv_dir]:inv.settings.epsabs=2e-13
  exactb=s.beta*X+inv_base.relative(X[None])[0];exactd=inv_dir.relative(X[None])[0]
  wf,df,of=fine.values(X);wc,dc,oc=coarseflow.values(X);wd,_,od=directionflow.values(X)
  out['interpolation_validation'].append({'point':X.tolist(),
    'base_velocity_fine_error':float(np.max(abs(wf-exactb))),
    'base_velocity_coarse_error':float(np.max(abs(wc-exactb))),
    'direction_velocity_fine_error':float(np.max(abs(wd-exactd))),
    'DW_resolution_difference':float(np.max(abs(df-dc))),
    'base_source_fine_error':float(abs(of-omega_base(*X))),
    'base_source_coarse_error':float(abs(oc-omega_base(*X))),
    'direction_source_fine_error':float(abs(od-omega_dir(*X))),
    'divergence_error':float(abs(np.trace(df)-2*s.beta))})
 out['cartesian_inverse']=[]
 for label,fn,inv in [('base',omega_base,inv_base),('direction',omega_dir,inv_dir)]:
  exact=inv.relative(points[[0,2,4]])
  for order in [12,18]:
   settings=InverseSettings(radius=12.,core_radial_order=order,core_angular_order=3*order,
       exterior_radial_order=4*order,exterior_angular_order=4*order,decay_power=decay)
   answer=CartesianInverse(fn,settings).relative(points[[0,2,4]])
   out['cartesian_inverse'].append({'field':label,'order':order,'points':points[[0,2,4]].tolist(),
    'modal_velocity':exact.tolist(),'Cartesian_velocity':answer.tolist(),
    'absolute_component_errors':abs(answer-exact).tolist(),'settings':settings.__dict__})
   save();print(now(),'Cartesian',label,order,'max_error',np.max(abs(answer-exact)),flush=True)
 out.update(stage='characteristics',reconstruction=[],responses=[]);save()
 cache={}
 def evaluate(point,h,cutoff,grid,tol):
  key=(*point,float(h),float(cutoff),grid,float(tol))
  if key not in cache:
   if h==0 and grid=='fine':f=fine
   elif h==0 and grid=='coarse':f=coarseflow
   else:f=flow(h,grid=='coarse')
   rr=reconstruct(f,point,s.beta,a0,cutoff=cutoff,rtol=tol,atol=tol*.01,compatible_seed=True)
   rr.update(parameter_offset=h,grid=grid)
   if rr['status']=='COMPLETE':
    seed=np.array(rr['seed_point']);rr['outgoing_flux']=float(f.W(seed)@seed/np.linalg.norm(seed))
   cache[key]=rr
  return cache[key]
 for X in points:
  for cutoff,grid,tol in [(.003,'fine',1e-10),(.001,'fine',1e-10),(.0003,'fine',1e-10),(.001,'coarse',1e-10),(.001,'fine',1e-12)]:
   rr=evaluate(X,0.,cutoff,grid,tol).copy()
   rr.update(stored_Theta=float(s.theta(*X)),stored_Omega=float(s.omega(*X)))
   if rr['status']=='COMPLETE':rr.update(Theta_difference=rr['Theta']-rr['stored_Theta'],Omega_difference=rr['Omega']-rr['stored_Omega'])
   out['reconstruction'].append(rr);save()
  for cutoff,grid,tol,step in [(.001,'fine',1e-10,2e-4),(.001,'fine',1e-10,1e-4),
    (.0003,'fine',1e-10,1e-4),(.001,'coarse',1e-10,1e-4),(.001,'fine',1e-12,1e-4)]:
   rows=[evaluate(X,j*step,cutoff,grid,tol) for j in [-2,-1,1,2]]
   response={'point':X.tolist(),'step':step,'cutoff':cutoff,'grid':grid,'rtol':tol,'evaluations':rows}
   if all(r['status']=='COMPLETE' for r in rows):
    vv=[vector(r) for r in rows];deriv=(vv[0]-8*vv[1]+8*vv[2]-vv[3])/(12*step)
    response.update(status='COMPLETE',derivative_Theta_gradient_Omega=deriv.tolist())
   else:response.update(status='FAILED')
   out['responses'].append(response);save()
  print(now(),'characteristic point',X.tolist(),'elapsed',out['elapsed_seconds'],flush=True)
 out['additional_quadrature_base']=inv_base.evidence;out['additional_quadrature_direction']=inv_dir.evidence
 out.update(status='COMPLETE',ended_utc=now(),stage='finished',
  scope='Finite-cutoff scalar map and projected source response on sampled flow tubes. No fitted coefficient projection, continuum Jacobian, uniform cutoff limit, a posteriori bounds, fixed point or B2 profile is established.')
 save();print(now(),'COMPLETE','elapsed',out['elapsed_seconds'],flush=True)

if __name__=='__main__':
 try:main()
 except Exception:
  (OUT/'failure.txt').write_text(datetime.now(timezone.utc).isoformat()+'\n'+traceback.format_exc())
  raise
