from pathlib import Path
import sympy as s
from datetime import datetime,timezone
import json
x,y,theta=s.symbols('x y theta',real=True)
G=-s.log(x*x+y*y)/(4*s.pi)
K=s.diff(G,x,2)
D=s.factor(s.diff(K,y))
expected=-y*(3*x*x-y*y)/(s.pi*(x*x+y*y)**3)
assert s.simplify(D-expected)==0
boundary=s.integrate(-s.cos(2*theta)*s.sin(theta)**2/(2*s.pi),(theta,0,2*s.pi))
assert boundary==s.Rational(1,4)
ratio=s.integrate(s.cos(theta)**2*s.sin(theta)**2,(theta,0,2*s.pi))/s.integrate(s.sin(theta)**2,(theta,0,2*s.pi))
assert ratio==s.Rational(1,4)
orthogonality=s.integrate(s.sin(3*theta)*s.sin(theta),(theta,0,2*s.pi))
assert orthogonality==0
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'off_origin_derivative':str(D),
'inner_boundary_jet_coefficient':str(boundary),'delta_hessian_jet_coefficient':'-1/2',
'final_local_coefficient':str(boundary-s.Rational(1,2)),
'gaussian_fourier_ratio':str(-ratio),'angular_orthogonality':str(orthogonality),'assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
