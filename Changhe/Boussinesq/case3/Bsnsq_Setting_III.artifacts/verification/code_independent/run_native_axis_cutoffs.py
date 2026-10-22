"""Own adaptive whole-plane inverse plus Hermite log-radius axis integration."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time,sys
import numpy as np
from scipy.interpolate import CubicHermiteSpline
from r2_state_values import R2State
from adaptive_modal_inverse import R2ModeSource,AdaptiveModalInverse,ModalSettings
from axis_cutoff_functional import functional
root=Path(sys.argv[1]);start=time.monotonic();m=json.loads((root/'manifest.json').read_text())
s=R2State(root/m['snapshot']);assert s.sha256==m['sha256']
if not s.native_source or float(s.meta['eps'])!=1:raise ValueError('This audit requires the explicitly serialized native fixed-source state with eps=1')
seed=R2ModeSource(s,kind='native_seed');src=R2ModeSource(s);lam=float(s.meta['lam']);center=s.center()
# Even indexed log points give the nested coarse grid. Spline cell endpoints and
# midpoints are included independently of either lane's quadrature collocation.
physical=[]
for ss in [s,s.seed_field]:
 t=np.unique(np.r_[ss.edges[1:-1],(ss.edges[1:]+ss.edges[:-1])/2]);rr=ss.L*np.sqrt(np.expm1(-2*ss.bb*np.log1p(-t)))
 physical.extend(rr[(rr>=1e-8)&(rr<=1e14)].tolist())
logs=np.linspace(-8.,14.,513);fine=np.unique(np.r_[10**logs,physical]);coarse=np.unique(np.r_[10**logs[::2],physical])
res={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','archive_sha256':s.sha256,'metadata':s.meta,
     'center':center,'fine_radii':len(fine),'coarse_radii':len(coarse),'runs':[],'method':'adaptive physical-radius full-plane inverse; Hermite log(v/r) with independently computed derivative; adaptive log-radius ODE quadrature',
     'limitations':'floating-point quadrature estimates and sampled interpolation study, not rigorous error bounds; no profile asserted'}
def save():
 res['elapsed_seconds']=time.monotonic()-start;(root/'results.json').write_text(json.dumps(res,indent=2)+'\n')
save();blocks={}
for name,source,decay in [('self',src,1/s.bb),('seed',seed,1/s.seed_field.bb)]:
 inv=AdaptiveModalInverse(source,source.count,ModalSettings(decay,1e-11,1e-11));n=inv.n
 cs=np.column_stack(((-1.)**n,np.ones(len(n))))
 values=[]
 for i,r in enumerate(fine):
  # epsabs/r is held fixed, so a tiny physical radius does not weaken strain accuracy.
  inv.settings.epsabs=1e-11*r
  pr,dp=inv.radial(r)
  # The signed radial velocity on each half-axis is -sum n pr cos(n phi).
  vv=-(n*pr)@cs/r;dv=-(n*(dp-pr))@cs/r
  values.append(np.r_[vv,dv])
  if i%80==0:print(name,i,'of',len(fine),'r',r,'elapsed',time.monotonic()-start,flush=True)
 data=np.array(values);blocks[name]=data
 np.savez_compressed(root/(name+'_axis.npz'),radii=fine,v_over_r=data[:,:2],vp=data[:,2:])
 bad=[q for q in inv.evidence if not(q['inner_success'] and q['outer_success'])]
 (root/(name+'_quadrature.json')).write_text(json.dumps(inv.evidence,indent=2)+'\n')
 res.setdefault('quadrature',{})[name]={'failed':bad,'count':len(inv.evidence)};save()
for kind,data in [('self',blocks['self']),('transport',blocks['self']+lam*blocks['seed'])]:
 for j,axis in enumerate(['up','down']):
  vr=s.beta+data[:,j];vp=s.beta+data[:,j+2]
  if np.any(vr<=0):
   res['runs'].append({'kind':kind,'axis':axis,'status':'NONPOSITIVE_VELOCITY','minimum_v_over_r':float(vr.min())});save();continue
  k=s.beta+center['c_self' if kind=='self' else 'c_mixed'];mu=1.5*s.beta+1
  for grid,rr in [('coarse',coarse),('fine',fine)]:
   ii=np.searchsorted(fine,rr);assert np.array_equal(fine[ii],rr)
   H=CubicHermiteSpline(np.log(rr),np.log(vr[ii]),vp[ii]/vr[ii]-1,extrapolate=False)
   vfun=lambda t:np.exp(H(t))
   for eps in [1e-4,1e-6,1e-8]:
    ans=functional(vfun,s.beta,center['F']['value'],eps,[1e2,1e4,1e6,1e8,1e10,1e12,1e14])
    ans.update(kind=kind,axis=axis,grid=grid,center_slope=k,center_slope_error=k-mu,
               exponent_h=2-2*mu/k,minimum_v_over_r=float(vr.min()),numerical_slope_at_rmin=float(vr[0]),
               slope_at_rmin_minus_center=float(vr[0]-k))
    res['runs'].append(ans);save()
    print(kind,axis,grid,'eps',eps,'Q1e8',ans['Q_raw'][3],'Q1e14',ans['Q_raw'][-1],flush=True)
res.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat())
res['code_hashes']={p:hashlib.sha256(Path('code_independent',p).read_bytes()).hexdigest() for p in ['run_native_axis_cutoffs.py','axis_cutoff_functional.py','adaptive_modal_inverse.py','r2_state_values.py']}
save();print('COMPLETE',res['elapsed_seconds'],flush=True)
