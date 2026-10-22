"""Controlled quadrature comparison using only the verifier's saved inverse.

The primary method remains adaptive log-radius ODE integration. A secondary
physical-radius trapezoid sequence isolates quadrature bias at identical cutoffs.
No fitting-lane code is imported, copied, or executed.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time,sys,hashlib
import numpy as np
from scipy.integrate import cumulative_trapezoid, trapezoid
from scipy.interpolate import CubicHermiteSpline
from r2_state_values import R2State
from adaptive_modal_inverse import R2ModeSource,AdaptiveModalInverse,ModalSettings
from axis_cutoff_functional import functional
root=Path(sys.argv[1]);start=time.monotonic()
m=json.loads((root/'manifest.json').read_text());s=R2State(root/m['snapshot']);assert s.sha256==m['sha256']
a=json.loads((root/'results.json').read_text());num=json.loads((root/'numerics_diagnostic_snapshot.json').read_text())
beta=s.beta;mu=1.5*beta+1;rho=(beta+1)/mu;P=(2*beta+1)/mu;ell=mu/beta;a0=s.center()['F']['value'];lam=float(s.meta['lam'])
out={'started_utc':datetime.now(timezone.utc).isoformat(),'archive_sha256':s.sha256,'status':'RUNNING','quadratures':[],'axis_value_checks':[],'refinement':[]}
d=np.load(root/'self_axis.npz');e=np.load(root/'seed_axis.npz');rr=d['radii'];assert np.array_equal(rr,e['radii'])
vr=beta+d['v_over_r']+lam*e['v_over_r'];vp=beta+d['vp']+lam*e['vp']
for j,axis in enumerate(['up','down']):
 H=CubicHermiteSpline(np.log(rr),np.log(vr[:,j]),vp[:,j]/vr[:,j]-1,extrapolate=False)
 ref=functional(lambda t:np.exp(H(t)),beta,a0,1e-4,[1e8],rtol=5e-12)
 for count in [1200,2400,4800,9600,19200]:
  r=np.geomspace(1e-4,1e8,count);V=np.exp(H(np.log(r)))
  Z=cumulative_trapezoid((mu/V-1)/r,r,initial=0.)
  logC=Z[-1]+(1-ell)*np.log(r[-1]);I=r[0]**(1-rho)/(1-rho)+trapezoid(np.exp(-rho*(np.log(r)+Z)),r)
  Q=(2*a0*beta/mu**2)*np.exp(-P*logC)*I
  out['quadratures'].append({'axis':axis,'points':count,'Q_physical_trapezoid':float(Q),'Q_adaptive_log_ODE':ref['Q_raw'][0],
    'relative_difference_from_adaptive':float(Q/ref['Q_raw'][0]-1),'C_R_physical_trapezoid':float(np.exp(logC)),
    'C_R_adaptive_log_ODE':ref['C_R'][0],'numerics_Q_reported':num['axis'][axis]['Q_closed_form_est'],
    'relative_difference_from_numerics':float(Q/num['axis'][axis]['Q_closed_form_est']-1)})
# Direct inverse at the six reported axis points, avoiding interpolation.
sources=[R2ModeSource(s),R2ModeSource(s,kind='native_seed')]
inverses=[AdaptiveModalInverse(q,q.count,ModalSettings(1/(s.bb if j==0 else s.seed_field.bb),1e-12,1e-12)) for j,q in enumerate(sources)]
for r in [.5,5.,500.]:
 fields=[]
 for inv in inverses:
  pr,dp=inv.radial(r);n=inv.n;cs=np.column_stack(((-1.)**n,np.ones(len(n))))
  # vr_signed = V2 on the upper axis and -V2 on the lower axis.
  signed_v=-(n*pr)@cs;du1dx=(n*(dp-pr))@cs/r
  fields.append((signed_v*np.array([1.,-1.]),du1dx))
 for j,axis in enumerate(['up','down']):
  value=fields[0][0][j]+lam*fields[1][0][j];der=fields[0][1][j]+lam*fields[1][1][j]
  q=num['axis_formula_check'][f'{axis}_r{r:g}']
  out['axis_value_checks'].append({'axis':axis,'r':r,'own_relative_V2':float(value),'own_dU1dx':float(der),
     'numerics_U2_formula':q['U2_formula'],'numerics_dU1dx_formula':q['dU1dx_formula'],
     'absolute_V2_difference':float(abs(value-q['U2_formula'])),'absolute_dU1dx_difference':float(abs(der-q['dU1dx_formula']))})
for q in a['runs']:
 if q.get('grid')!='fine':continue
 c=next(p for p in a['runs'] if p.get('grid')=='coarse' and all(p.get(k)==q[k] for k in ['kind','axis','epsilon']))
 out['refinement'].append({k:q[k] for k in ['kind','axis','epsilon']}|{'max_relative_Q_raw_difference':float(np.max(np.abs(np.array(c['Q_raw'])/q['Q_raw']-1))),
   'max_relative_C_R_difference':float(np.max(np.abs(np.array(c['C_R'])/q['C_R']-1)))})
out['quadrature_estimates']=[{'source':name,'values':inv.evidence} for name,inv in zip(['self','seed'],inverses)]
out.update(status='COMPLETE',elapsed_seconds=time.monotonic()-start,ended_utc=datetime.now(timezone.utc).isoformat())
out['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
(root/'quadrature_comparison.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='quadrature_estimates'},indent=2))
