"""Independent symbolic and sharpness controls for P218; not a profile solver."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
import sympy as s
v=Path('research/218_separable_temperature_foliation/verification');now=datetime.now(timezone.utc).isoformat();start=time.monotonic()
k,y,x=s.symbols('k y x',real=True);a=s.Function('a')(y);w=s.Function('w')(k,y);z=s.Function('z')(k,y);H=s.Function('H')(k)
Q=w-k*s.diff(a,y)*z
# Physical derivatives after pullback: Dx=1/a Dk, Dy=Dy|k-k a'/a Dk.
Dx=lambda f:s.diff(f,k)/a
Dy=lambda f:s.diff(f,y)-k*s.diff(a,y)/a*s.diff(f,k)
checks={}
def check(n,e):
 e=s.simplify(e);checks[n]={'difference':str(e),'pass':e==0}
check('divergence_change_of_variables',Dx(w)+Dy(z)-(s.diff(Q,k)+s.diff(a*z,y))/a)
check('temperature_transport',w*Dx(H)+z*Dy(H)-s.diff(H,k)*Q/a)
check('differentiate_limit_identity',s.diff(2*a*a/s.diff(a,y),y)-(4*a-2*a*a*s.diff(a,y,2)/s.diff(a,y)**2))
# C1 H need only a neighborhood of each k_j, as used in the proof. Smooth example.
h=k*k/(1+k*k)
check('example_H_derivative',s.diff(h,k)-2*k/(1+k*k)**2)
check('example_H_center_coefficient',s.diff(h,k,2).subs(k,0)-2)
# Removing nonconstant-H hypothesis permits any positive scale, since constant theta.
check('constant_temperature_transport',2*x*s.diff(s.Integer(1),x)+2*y*s.diff(s.Integer(1),y))
check('radial_dilation_divergence',s.diff(2*x,x)+s.diff(2*y,y)-4)
# Half-plane y>-1: a=y+1 is positive, W=(2x,2(y+1)) is tangent to k=x/a.
kh=x/(y+1)
check('halfplane_affine_example_transport',2*x*s.diff(kh,x)+2*(y+1)*s.diff(kh,y))
check('halfplane_affine_example_divergence',s.diff(2*x,x)+s.diff(2*(y+1),y)-4)
# Positive globally a=exp(y): tangency + divergence force W1/x=4+C exp(-y),
# hence fixed-height horizontal limit cannot equal2 simultaneously at all heights.
C=s.symbols('C');ap=s.exp(y);Ap=s.exp(y)-1
ratio=s.diff(ap,y)*(4*Ap+C)/(ap**2)
check('exponential_scale_forced_ratio',ratio-(4+(C-4)*s.exp(-y)))
check('incompatible_exponential_height_limits',ratio.subs(C,2).subs(y,s.log(2))-3)
result={'started_utc':now,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':checks,'all_passed':all(t['pass'] for t in checks.values()),'scope':'Symbolic identities and logical hypothesis controls; complete global proof is PROOF.md. Half-plane and constant-H controls are not B2 profiles.','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(v/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(len(checks),'checks',result['all_passed'],result['elapsed_seconds']);assert result['all_passed']
