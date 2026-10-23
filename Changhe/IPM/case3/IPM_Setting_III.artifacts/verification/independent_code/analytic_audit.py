"""Independent symbolic audit of the lead's v0 formulas; no lane imports."""
import json
from pathlib import Path
import sympy as s
x,y,theta = s.symbols('x y theta', real=True)
a,b,e,c,cl,q1,q2=s.symbols('a b e c cl q1 q2', real=True)
rho=a*y+b*x*x*y+e*y**3
psi=c*x*y+q1*x**3*y+q2*x*y**3
U=s.Matrix([-s.diff(psi,y),s.diff(psi,x)])
W=s.Matrix([cl*x,cl*y])+U
res=s.expand(W.dot(s.Matrix([s.diff(rho,x),s.diff(rho,y)]))-rho)
poisson=s.expand(-s.diff(psi,x,2)-s.diff(psi,y,2)-s.diff(rho,x))
boundary=s.integrate(a*s.sin(theta)*s.sin(3*theta)*(cl-c*s.cos(2*theta)),(theta,0,2*s.pi))
jet = s.solve([res.coeff(y,1).coeff(x,0), res.coeff(x,2).coeff(y,1),res.coeff(y,3).coeff(x,0),poisson.coeff(x,1).coeff(y,1)],[c,q1,q2,e],dict=True)
ans={'symbolic_center_solutions':[{str(k):str(s.factor(v)) for k,v in sol.items()} for sol in jet], 'outward_radial_origin_boundary':str(boundary),'annulus_inner_boundary_after_center_relation':str(s.simplify((-boundary).subs(c,1-cl))),'claimed_v0_boundary':str(a*(cl-1)*s.pi/2),'audit':'v0 I5 has the opposite sign to the annulus inner boundary.'}
print(json.dumps(ans,indent=2))
Path('research/origin/verification/symbolic_audit.json').write_text(json.dumps(ans,indent=2)+'\n')
