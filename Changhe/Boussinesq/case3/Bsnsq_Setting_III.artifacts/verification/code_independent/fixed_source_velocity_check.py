"""Own whole-plane velocity tail and cutoff check of archived seed forcing."""
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy.integrate import quad
from scipy.special import expit
import json,hashlib,shutil,sys,time
from r2_state_values import R2State
from adaptive_modal_inverse import AdaptiveModalInverse,ModalSettings,R2ModeSource
root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True);start=time.monotonic()
src=Path('verification/additive_driver_20261020T2128/lambda_seed_snapshot.npz');s=R2State(src)
g=R2ModeSource(s);e=R2ModeSource(s,True);modes=lambda r:e(r)-g(r)
nu=1/s.bb;n=np.arange(1,s.K+1);p=2-nu
# Derive the finite sine tail directly from endpoint values, not inverse samples.
z=np.asarray(s.Es(1.)-s.Gs(1.));a=np.zeros(s.K);a[0]=z[0]
for k in range(1,s.K):
 a[k]+=.5*z[k]
 if k>=2:a[k-2]-=.5*z[k]
a*=s.L**(1+nu);coeff=a/(n*n-p*p)
phis=np.linspace(0,2*np.pi,33)[:-1];sn=np.sin(phis);cs=np.cos(phis)
vr=-(n*coeff)@np.cos(n[:,None]*phis);vt=(p*coeff)@np.sin(n[:,None]*phis)
va=np.stack((vr*sn+vt*cs,-vr*cs+vt*sn),axis=-1)
inv=AdaptiveModalInverse(modes,s.K,ModalSettings(nu,1e-10,1e-10))
out=dict(started_utc=datetime.now(timezone.utc).isoformat(),status='RUNNING',seed_sha256=s.sha256,beta_seed=s.bb,nu=nu,angular_modes=a.tolist(),stream_coefficients=coeff.tolist(),tail_rows=[],cutoff_rows=[],angles=phis.tolist(),predicted_velocity=va.tolist())
for r in [1e2,1e3,1e4,1e6,1e8,1e10]:
 pts=np.stack((r*sn,-r*cs),axis=-1);actual=inv.relative(pts)/r**(1-nu)
 err=np.max(np.linalg.norm(actual-va,axis=1));out['tail_rows'].append(dict(r=r,max_vector_error=float(err),scaled_velocity_max=float(np.max(np.linalg.norm(actual,axis=1))),predicted_max=float(np.max(np.linalg.norm(va,axis=1)))))
 print('tail',r,err,flush=True)
# Core points are all inside the region where Psi_b=xy exactly.
pts=np.array([[.2,.3],[.5,-.2],[.1,.8]]);ref=inv.relative(pts)
def chi(q):
 if q<=1:return 1.
 if q>=2:return 0.
 return float(expit(1/(q-1)-1/(2-q)))
for R in [16.,32.,64.,128.,256.,512.]:
 cut=lambda r:chi(r/R)*modes(r)
 cinv=AdaptiveModalInverse(cut,s.K,ModalSettings(nu,1e-10,1e-10))
 err=cinv.relative(pts)-ref
 # Missing center strain directly from the far radial mode integral, with
 # r=R t^(-1/nu). c[fS]-c[fR] = -1/2 int (1-chi)H2 dr/r.
 def tail_strain(t):
  r=R*t**(-1/nu)
  return -(1-chi(r/R))*modes(r)[1]/(2*nu*t)
 dc,dcerr=quad(tail_strain,0,1,epsabs=2e-12,epsrel=2e-12,limit=400)
 vb=np.stack((-pts[:,0],pts[:,1]),axis=-1)
 matched=err+dc*vb
 out['cutoff_rows'].append(dict(R=R,missing_strain=float(dc),strain_quad_error=float(dcerr),max_velocity_error=float(np.max(np.linalg.norm(err,axis=1))),max_matched_error=float(np.max(np.linalg.norm(matched,axis=1))),scaled_raw_error=float(R**nu*np.max(np.linalg.norm(err,axis=1))),scaled_matched_error=float(R**(1+nu)*np.max(np.linalg.norm(matched,axis=1))),inverse_flags_all=all(q['inner_success'] and q['outer_success'] for q in cinv.evidence)))
 print('cutoff',R,out['cutoff_rows'][-1]['max_velocity_error'],out['cutoff_rows'][-1]['max_matched_error'],flush=True)
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,quadrature=inv.evidence,inverse_flags_all=all(q['inner_success'] and q['outer_success'] for q in inv.evidence),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),limitations='Floating-point quadrature and finite angle samples, not an interval certificate. Exact finite source is specified by the immutable seed archive. No field is asserted to solve B2.')
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
for name in ['fixed_source_velocity_check.py','r2_state_values.py','adaptive_modal_inverse.py']:shutil.copyfile(Path('code_independent')/name,root/name)
print('COMPLETE',out['elapsed_seconds'],flush=True)
