"""Independent monotonicity diagnostics for archived temperature fields."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,sys,time
import numpy as np
from r2_state_values import R2State
from finite_difference import stencil
from exact_tail_residuals import endpoints,chebs,linear,mul,add,scale,deriv,COS,SIN,COS2,exactpoint,ser,evalfloat
root=Path(sys.argv[1]);root.mkdir(exist_ok=True)
manifest=json.loads((root/'manifest.json').read_text());start=time.monotonic()
z,weights=stencil()
out={'started_utc':datetime.now(timezone.utc).isoformat(),'states':[],'scope':'archived nonsolutions, sampled positivity only; exact negative tail witness excludes monotonicity but positive samples do not prove it'}
for item in manifest['states']:
 s=R2State(item['snapshot']);tm=(s.edges[:-1]+s.edges[1:])/2
 radii=np.unique(np.r_[np.geomspace(1e-6,1e10,150),s.L*np.sqrt(np.expm1(-2*s.bb*np.log1p(-tm)))])
 radii=radii[radii<1e11]
 th=np.linspace(-np.pi/2,np.pi/2,99)[1:-1]
 x=(radii[:,None]*np.cos(th)).ravel();y=(radii[:,None]*np.sin(th)).ravel();rr=np.repeat(radii,len(th))
 f=s.divided(x,y,'F');row={'label':item['label'],'source_sha256':s.sha256,'beta':s.beta,'basis':s.bb,'points':len(x),'steps':[]}
 for h in (2e-5,1e-5):
  hh=h*np.maximum(1.,rr);xx=x[:,None]+hh[:,None]*z;yy=np.broadcast_to(y[:,None],xx.shape)
  fx=s.divided(xx,yy,'F')@weights/hh;d=2*f+x*fx
  i=int(np.argmin(d/(2*abs(f)+abs(x*fx))));j=int(np.argmin(f))
  row['steps'].append({'h':h,'F_negative_count':int((f<0).sum()),'S_negative_count':int((d<0).sum()),'S_min_relative':float((d/(2*abs(f)+abs(x*fx)))[i]),'S_worst_point':[float(x[i]),float(y[i])],'F_min':float(f[j]),'F_min_point':[float(x[j]),float(y[j])]})
 vals,_=endpoints(s,s.rawF);pol=chebs(s.K);H=mul(COS2,linear(vals,pol));m=1-2/Q.from_float(s.bb)
 D=add(scale(mul(COS,H),m),scale(mul(SIN,deriv(H)),Q(-1)))
 ang=np.linspace(-np.pi/2,np.pi/2,4001)[1:-1]
 sampled=evalfloat(D,ang);neg=[]
 for j in range(-199,200):
  t=Q(j,200);cx=(1-t*t)/(1+t*t);sy=2*t/(1+t*t);v=exactpoint(D,cx,sy)
  if v<0:neg.append({'cos_theta':str(cx),'sin_theta':str(sy),'value':str(v),'float_value':float(v)});break
 row['tail']={'Theta_x_angular_coefficients':ser(D),'sampled_min':float(sampled.min()),'sampled_max':float(sampled.max()),'negative_rational_witness':neg[0] if neg else None,'positive_L_power_omitted':'L^(1+2/b)'}
 out['states'].append(row);print(item['label'],row['steps'][-1],bool(neg),flush=True)
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
