"""Physical G^2 r dr diagnostics via r=L sinh(u), independent of z weights.
No fitting-lane code imports; exact certificates remain the rigorous evidence.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time
import numpy as np
from r2_state_values import R2State
start=time.monotonic();base=Path('verification/full_modal_norm_20261021T1730Z');phi=2*np.pi*(np.arange(96)+.413)/96

def grid(edges,order):
 q,w=np.polynomial.legendre.leggauss(order)
 u=np.concatenate([(a+b)/2+(b-a)*q/2 for a,b in zip(edges[:-1],edges[1:])])
 weights=np.concatenate([(b-a)*w/2 for a,b in zip(edges[:-1],edges[1:])]);return u,weights

def physical_norm(values,r,jac,weights,b,L):
 return float(2*np.dot(weights*r*jac,np.mean(values**2,axis=1))/(b*L*L))

rows=[]
for p in sorted(x for x in base.iterdir()if x.is_dir()):
 inputs=[json.loads((p/f'input{i}.json').read_text())for i in range(2)];states=[R2State(x['archive_path'])for x in inputs];a,b=states
 assert a.bb==b.bb and a.L==b.L and a.degree==b.degree and np.array_equal(a.knots,b.knots)
 cert=json.loads((p/'certificate.json').read_text());target=np.array([[float((Q(v[0])+Q(v[1]))/2)for v in row]for row in cert['norm_squared_over_pi_b_L2']]);bb=a.bb;L=a.L
 z=1-a.edges[:-1];knots=np.arcsinh(np.sqrt(np.expm1(-2*bb*np.log(z))))
 edges=np.unique(np.r_[np.linspace(0,120,121),knots]);checks=[]
 for order in [32,64]:
  u,w=grid(edges,order);r=L*np.sinh(u);jac=L*np.cosh(u);vals=[]
  for s in states:
   radial=s.radial(r,'G');k=np.arange(s.K);vals.append([radial@np.cos(k[:,None]*phi),radial@(-k[:,None]*np.sin(k[:,None]*phi))])
  vals.append([x-y for x,y in zip(*vals)])
  got=np.array([[physical_norm(v,r,jac,w,bb,L)for v in pair]for pair in vals]);err=np.abs(got-target)/target
  assert np.max(err)<2e-8,(p,err)
  checks.append({'order':order,'radial_nodes':len(r),'physical_norm_squared_over_pi_b_L2':got.tolist(),'max_relative_error':float(np.max(err))})
 rows.append({'pair':p.name,'checks':checks,'coarse_fine_relative_difference':(np.abs(np.array(checks[0]['physical_norm_squared_over_pi_b_L2'])-np.array(checks[1]['physical_norm_squared_over_pi_b_L2']))/target).tolist()})
controls=[]
u,w=grid(np.linspace(0,120,121),40)
for L in [1.,1.5,2.75]:
 r=L*np.sinh(u);jac=L*np.cosh(u);bb=61/20;z=(1+(r/L)**2)**(-1/(2*bb));rho=r/np.hypot(r,L)
 for k in [0,1,2,5]:
  for m in [0,2,5]:
   radial=z**(bb+1+m)*(rho if k%2 else 1);v=radial[:,None]*np.cos(k*phi)
   expected=(2 if k==0 else 1)*(1/(2*m+2)-(1/(2*m+2*bb+2)if k%2 else 0))
   got=physical_norm(v,r,jac,w,bb,L);assert abs(got-expected)<1e-12
   controls.append({'L':L,'k':k,'m':m,'measured':got,'expected':expected,'absolute_error':abs(got-expected)})
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'verdict':'PASS diagnostic physical-radius normalization checks','method':'Direct sampled G^2 r dr with r=L sinh(u), jacobian L cosh(u), no z-weight or divided-envelope cancellation. Full96-angle trapezoid. u cutoff120 is finite and its tail is not interval bounded here.','rows':rows,'manufactured_controls':controls,'scope':'Floating consistency only. Decoder is own R2State, not shared with certificate generator or checker; NumPy knot reconstruction and SciPy libraries remain common infrastructure. No runtime clipping or historical binary identity claim.','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
p=Path('research/187_full_modal_L2_certificates/verification/physical_radius_checks.json');p.write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],'PASS',out['elapsed_seconds'],'manufactured',len(controls),'maxrelative',max(c['max_relative_error']for x in rows for c in x['checks']))
